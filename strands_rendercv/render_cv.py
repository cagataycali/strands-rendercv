"""
Strands RenderCV Tool - CV/Resume Generator

A tool that wraps the RenderCV package for generating
professional CVs and resumes with strict validation and error handling.
"""

import json
import pathlib
import tempfile
from typing import Any, Dict, Optional

from strands import tool


@tool
def render_cv(
    action: str,
    input_file: Optional[str] = None,
    cv_data: Optional[str] = None,
    design_file: Optional[str] = None,
    locale_file: Optional[str] = None,
    settings_file: Optional[str] = None,
    output_dir: Optional[str] = None,
    typst_path: Optional[str] = None,
    pdf_path: Optional[str] = None,
    markdown_path: Optional[str] = None,
    html_path: Optional[str] = None,
    png_path: Optional[str] = None,
    dont_generate_typst: bool = False,
    dont_generate_pdf: bool = False,
    dont_generate_markdown: bool = False,
    dont_generate_html: bool = False,
    dont_generate_png: bool = False,
    overrides: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Generate professional CVs/resumes using RenderCV with strict validation.

    This tool provides full access to the RenderCV package functionality:
    - Validate CV YAML/JSON against schema
    - Generate PDFs with perfect typography
    - Support multiple themes and customization
    - Detailed validation errors like use_aws

    Returns:
        Dict with status and content:
            - status: "success" or "error"
            - content: List with text responses, file paths, or validation errors

    Examples:
        # Validate CV data
        render_cv(action="validate", input_file="cv.yaml")

        # Generate CV with all outputs
        render_cv(action="render", input_file="cv.yaml")

        # Generate only PDF (skip PNG/HTML/Markdown)
        render_cv(
            action="render",
            input_file="cv.yaml",
            dont_generate_png=True,
            dont_generate_html=True,
            dont_generate_markdown=True
        )

        # Use custom design
        render_cv(
            action="render",
            input_file="cv.yaml",
            design_file="custom_design.yaml"
        )

        # Override specific fields
        render_cv(
            action="render",
            input_file="cv.yaml",
            overrides='{"cv.phone": "+1 234 567 8900", "cv.email": "new@email.com"}'
        )

        # Create from JSON data directly
        render_cv(
            action="render",
            cv_data='{"cv": {"name": "John Doe", "email": "john@example.com"}, ...}'
        )
    """
    try:
        # Import required modules
        from ruamel.yaml import YAML
        from rendercv.cli.render_command.run_rendercv import run_rendercv
        from rendercv.cli.render_command.progress_panel import ProgressPanel
        from rendercv.schema.rendercv_model_builder import (
            build_rendercv_dictionary_and_model,
            BuildRendercvModelArguments,
        )
        from rendercv.exception import (
            RenderCVUserValidationError,
            RenderCVUserError,
        )
        from rendercv.schema.json_schema_generator import generate_json_schema
        from rendercv.schema.sample_generator import create_sample_yaml_input_file

        # Set output directory
        if output_dir:
            output_path = pathlib.Path(output_dir).resolve()
            output_path.mkdir(parents=True, exist_ok=True)
        else:
            output_path = pathlib.Path.cwd()

        # Handle actions
        if action == "list_themes":
            themes = [
                "classic",
                "engineeringresumes",
                "sb2nov",
                "moderncv",
                "engineeringclassic",
            ]
            return {
                "status": "success",
                "content": [
                    {
                        "text": "Available RenderCV themes:\n\n"
                        + "\n".join(f"  • {theme}" for theme in themes)
                        + "\n\nSet theme in design.theme field or use design_file parameter."
                    }
                ],
            }

        elif action == "get_schema":
            schema = generate_json_schema()
            return {
                "status": "success",
                "content": [
                    {
                        "text": f"RenderCV JSON Schema:\n\n```json\n{json.dumps(schema, indent=2)}\n```"
                    }
                ],
            }

        elif action == "help":
            help_text = """
RenderCV Tool - Comprehensive Guide

QUICK START:
1. Create template: render_cv(action="create_template")
2. Edit YAML file with your information
3. Validate: render_cv(action="validate", input_file="cv.yaml")
4. Generate: render_cv(action="render", input_file="cv.yaml")

REQUIRED FIELDS:
- cv.name (only required field!)

OPTIONAL FIELDS:
- cv.headline, location, email, phone, website, summary
- cv.social_networks: [{network, username}]
- design.theme: classic/engineeringresumes/sb2nov/moderncv/engineeringclassic
- design.page: margins, size, colors, typography
- sections: work_experience, education, projects, publications, etc.

VALIDATION:
The tool validates all data against RenderCV's strict schema.
Errors show:
- Field location (e.g., cv.sections.work_experience[0].start_date)
- Line/column in YAML file
- Detailed error message
- Input value that caused error

COMMON VALIDATION ERRORS:
- Invalid date format → Use "YYYY-MM" or "YYYY-MM-DD" or "present"
- Invalid phone format → Use "+1 234 567 8900" (optional field)
- Missing cv.name → Required field
- Invalid theme → Use one from list_themes
- Invalid URL → Must be valid URL format

OVERRIDES:
Use overrides parameter to modify fields without editing YAML:
  overrides='{"cv.phone": "+1234567890", "cv.email": "new@email.com"}'

OUTPUTS:
By default, generates all formats:
- Typst (.typ) - intermediate format
- PDF (.pdf) - main output
- Markdown (.md) - text format
- HTML (.html) - web format
- PNG (.png) - images (one per page)

Skip specific outputs with dont_generate_* parameters.

DOCUMENTATION:
Full docs: https://docs.rendercv.com
Schema: render_cv(action="get_schema")
"""
            return {"status": "success", "content": [{"text": help_text}]}

        elif action == "create_template":
            # Use RenderCV's built-in sample generator
            sample_yaml = create_sample_yaml_input_file(
                file_path=None, name="John Doe", theme="classic", locale="english"
            )
            template_file = output_path / "John_Doe_CV.yaml"

            with open(template_file, "w") as f:
                f.write(sample_yaml)

            return {
                "status": "success",
                "content": [
                    {
                        "text": f"✅ Template created: {template_file}\n\n"
                        f"Next steps:\n"
                        f"1. Edit the template with your information\n"
                        f"2. Validate: render_cv(action='validate', input_file='{template_file}')\n"
                        f"3. Render: render_cv(action='render', input_file='{template_file}')"
                    }
                ],
            }

        elif action in ["validate", "render"]:
            # Prepare input
            temp_file = None
            if input_file:
                input_path = pathlib.Path(input_file).resolve()
                if not input_path.exists():
                    return {
                        "status": "error",
                        "content": [{"text": f"❌ Input file not found: {input_file}"}],
                    }
            elif cv_data:
                # Create temporary file from cv_data
                try:
                    # Try to parse as JSON first
                    data_dict = json.loads(cv_data)
                except json.JSONDecodeError:
                    # Maybe it's YAML format
                    yaml = YAML()
                    try:
                        data_dict = yaml.load(cv_data)
                    except Exception as e:
                        return {
                            "status": "error",
                            "content": [
                                {
                                    "text": f"❌ Invalid cv_data format (not JSON or YAML):\n{e}"
                                }
                            ],
                        }

                temp_file = output_path / "temp_cv_input.yaml"
                yaml = YAML()
                yaml.default_flow_style = False
                with open(temp_file, "w") as f:
                    yaml.dump(data_dict, f)
                input_path = temp_file
            else:
                return {
                    "status": "error",
                    "content": [
                        {"text": "❌ Either 'input_file' or 'cv_data' is required"}
                    ],
                }

            # Build arguments for RenderCV
            kwargs: BuildRendercvModelArguments = {}

            if design_file:
                kwargs["design_file_path_or_contents"] = pathlib.Path(
                    design_file
                ).resolve()
            if locale_file:
                kwargs["locale_file_path_or_contents"] = pathlib.Path(
                    locale_file
                ).resolve()
            if settings_file:
                kwargs["settings_file_path_or_contents"] = pathlib.Path(
                    settings_file
                ).resolve()
            if typst_path:
                kwargs["typst_path"] = pathlib.Path(typst_path)
            if pdf_path:
                kwargs["pdf_path"] = pathlib.Path(pdf_path)
            if markdown_path:
                kwargs["markdown_path"] = pathlib.Path(markdown_path)
            if html_path:
                kwargs["html_path"] = pathlib.Path(html_path)
            if png_path:
                kwargs["png_path"] = pathlib.Path(png_path)

            # Generation flags
            if dont_generate_typst:
                kwargs["dont_generate_typst"] = True
            if dont_generate_pdf:
                kwargs["dont_generate_pdf"] = True
            if dont_generate_markdown:
                kwargs["dont_generate_markdown"] = True
            if dont_generate_html:
                kwargs["dont_generate_html"] = True
            if dont_generate_png:
                kwargs["dont_generate_png"] = True

            # Overrides
            if overrides:
                try:
                    overrides_dict = json.loads(overrides)
                    kwargs["overrides"] = overrides_dict
                except json.JSONDecodeError as e:
                    return {
                        "status": "error",
                        "content": [
                            {"text": f"❌ Invalid overrides JSON format:\n{e}"}
                        ],
                    }

            # Validate or render
            try:
                if action == "validate":
                    # Just validate without generating outputs
                    _, model = build_rendercv_dictionary_and_model(input_path, **kwargs)
                    result_text = f"✅ Validation successful!\n\n"
                    result_text += f"CV Name: {model.cv.name}\n"
                    if getattr(model.cv, 'headline', None):
                        result_text += f"Headline: {model.cv.headline}\n"
                    if getattr(model.cv, 'location', None):
                        result_text += f"Location: {model.cv.location}\n"
                    result_text += f"Theme: {model.design.theme}\n"
                    result_text += f"\nSections: {', '.join(model.cv.sections.keys())}\n"
                    result_text += f"\n✓ Ready to render!"

                    if temp_file and temp_file.exists():
                        temp_file.unlink()

                    return {
                        "status": "success",
                        "content": [{"text": result_text}],
                    }

                else:  # action == "render"
                    # Generate all outputs
                    import io
                    import sys

                    # Capture progress output
                    progress = ProgressPanel(quiet=False)
                    
                    # Save current directory and change to output directory
                    import os
                    original_dir = os.getcwd()
                    os.chdir(output_path)

                    try:
                        run_rendercv(input_path, progress, **kwargs)
                        
                        # Restore directory
                        os.chdir(original_dir)

                        # Clean up temp file
                        if temp_file and temp_file.exists():
                            temp_file.unlink()

                        # Find generated files
                        generated_files = []
                        extensions = []
                        
                        if not dont_generate_pdf:
                            extensions.append("*.pdf")
                        if not dont_generate_typst:
                            extensions.append("*.typ")
                        if not dont_generate_markdown:
                            extensions.append("*.md")
                        if not dont_generate_html:
                            extensions.append("*.html")
                        if not dont_generate_png:
                            extensions.append("*.png")

                        for ext in extensions:
                            generated_files.extend(output_path.glob(ext))

                        result_text = "✅ CV generated successfully!\n\n"
                        result_text += "Generated files:\n"
                        for f in sorted(generated_files):
                            result_text += f"  📄 {f}\n"
                        
                        if generated_files:
                            pdf_files = [f for f in generated_files if f.suffix == ".pdf"]
                            if pdf_files:
                                result_text += f"\n📱 Open PDF: open {pdf_files[0]}"

                        return {
                            "status": "success",
                            "content": [{"text": result_text}],
                        }

                    except Exception as e:
                        os.chdir(original_dir)
                        if temp_file and temp_file.exists():
                            temp_file.unlink()
                        raise e

            except RenderCVUserValidationError as e:
                # Clean up temp file
                if temp_file and temp_file.exists():
                    temp_file.unlink()

                # Format validation errors (similar to use_aws error formatting)
                error_text = "❌ Validation Error:\n\n"
                error_text += f"Found {len(e.validation_errors)} validation error(s):\n\n"

                for i, err in enumerate(e.validation_errors, 1):
                    error_text += f"Error {i}:\n"
                    error_text += f"  Location: {'.'.join(err.location)}\n"
                    if err.yaml_location:
                        line_start, col_start = err.yaml_location[0]
                        line_end, col_end = err.yaml_location[1]
                        error_text += f"  Line: {line_start + 1}, Column: {col_start + 1}\n"
                    error_text += f"  Message: {err.message}\n"
                    if err.input:
                        error_text += f"  Input: {err.input}\n"
                    error_text += "\n"

                error_text += "\nCommon fixes:\n"
                error_text += "• Dates: Use 'YYYY-MM' or 'YYYY-MM-DD' or 'present'\n"
                error_text += "• Phone: Use '+1 234 567 8900' (optional field)\n"
                error_text += "• URLs: Must be valid URL format\n"
                error_text += "• Required: cv.name is the only required field\n"
                error_text += "\nFor help: render_cv(action='help')"

                return {
                    "status": "error",
                    "content": [{"text": error_text}],
                }

            except RenderCVUserError as e:
                if temp_file and temp_file.exists():
                    temp_file.unlink()

                return {
                    "status": "error",
                    "content": [{"text": f"❌ RenderCV Error:\n\n{e.message}"}],
                }

            except Exception as e:
                if temp_file and temp_file.exists():
                    temp_file.unlink()

                return {
                    "status": "error",
                    "content": [{"text": f"❌ Unexpected error:\n\n{str(e)}"}],
                }

        else:
            return {
                "status": "error",
                "content": [
                    {
                        "text": f"❌ Unknown action: {action}\n\n"
                        "Valid actions: render, validate, create_template, list_themes, get_schema, help"
                    }
                ],
            }

    except ImportError as e:
        return {
            "status": "error",
            "content": [
                {
                    "text": f"❌ Missing dependency: {e}\n\n"
                    "Install with: pip install 'rendercv[full]' ruamel.yaml"
                }
            ],
        }
    except Exception as e:
        return {
            "status": "error",
            "content": [{"text": f"❌ Error: {str(e)}"}],
        }
