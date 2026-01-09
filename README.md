# strands-rendercv

[![PyPI version](https://badge.fury.io/py/strands-rendercv.svg)](https://pypi.org/project/strands-rendercv/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

**CV generation with Strands Agents + RenderCV**

Generate beautiful, typographically perfect CVs from YAML. AI reads your docs, validates schema, outputs PDF.

---

## Installation

```bash
pip install strands-rendercv

# macOS: Install LaTeX for PDF generation
brew install --cask mactex-no-gui
```

---

## Quick Start

```python
from strands import Agent
from strands_rendercv import render_cv

agent = Agent(tools=[render_cv])

# Create template → Edit → Generate
agent.tool.render_cv(action="create_template")
agent.tool.render_cv(action="validate", input_file="John_Doe_CV.yaml")
agent.tool.render_cv(action="render", input_file="John_Doe_CV.yaml")
```

---

## AI-Powered Generation

```python
agent("""
Read my LinkedIn from ~/linkedin.md and work log from ~/work-log.md.
Generate CV for ... Engineer at ....
Focus on: distributed systems, leadership, open source.
Use 'engineeringresumes' theme.
""")
```

**What happens:**
1. AI reads your docs
2. Extracts + structures data as YAML
3. Validates schema
4. Generates PDF + HTML + Markdown

---

## Examples

5 production-ready templates in [`examples/`](examples/):

- **Senior SWE** - Full-stack, distributed systems ([YAML](examples/senior_swe_cv.yaml))
- **ML Researcher** - PhD, publications ([YAML](examples/ml_researcher_cv.yaml))
- **Product Designer** - UX/UI, design systems ([YAML](examples/product_designer_cv.yaml))
- **Startup Founder** - Exits, fundraising ([YAML](examples/startup_founder_cv.yaml))
- **DevRel Engineer** - Community, content ([YAML](examples/devrel_engineer_cv.yaml))

```python
agent.tool.render_cv(action="render", input_file="examples/senior_swe_cv.yaml")
```

---

## Actions

| Action | Description |
|--------|-------------|
| `create_template` | Generate sample YAML |
| `validate` | Check schema before render |
| `render` | Generate PDF + HTML + MD |
| `list_themes` | Show available themes |

---

## YAML Structure

```yaml
cv:
  name: Jane Doe  # Only required field
  headline: Senior Software Engineer
  email: jane@example.com
  
  social_networks:
    - network: GitHub
      username: janedoe
  
  sections:
    work_experience:
      - company: Tech Corp
        position: Staff Engineer
        start_date: 2020-01
        end_date: present
        highlights:
          - "Built distributed tracing system (1B+ events/day)"
          - "Reduced P99 latency by 80%"
    
    education:
      - institution: Stanford
        degree: MS
        area: Computer Science
        start_date: 2016-09
        end_date: 2018-06

design:
  theme: engineeringresumes  # or classic, sb2nov, moderncv
```

---

## Advanced

**Override fields:**
```python
render_cv(
    action="render",
    input_file="cv.yaml",
    overrides='{"cv.email": "work@company.com"}'
)
```

**PDF only (faster):**
```python
render_cv(
    action="render",
    input_file="cv.yaml",
    dont_generate_png=True,
    dont_generate_html=True
)
```

**Multi-target generation:**
```python
for company in ["google", "meta", "openai"]:
    agent(f"Customize my CV for {company}, output to ./{company}/")
```

---

## Common Issues

**Validation fails:**
- Use `YYYY-MM` or `YYYY-MM-DD` or `present` for dates
- Phone format: `+1 234 567 8900` (optional)
- Social networks: LinkedIn, GitHub, X (not Twitter)
- Page size: `us-letter` (not letterpaper)

**Empty CV:**
- Sections must be under `cv.sections`, not at root
- Avoid special chars: `#`, `%`

---

## Citation

```bibtex
@software{strands_rendercv2026,
  author = {Cagatay Cali},
  title = {strands-rendercv: AI-Powered Professional CV Generation},
  year = {2026},
  url = {https://github.com/cagataycali/strands-rendercv},
  note = {Built with Strands Agents and RenderCV}
}
```

---

**Built with:** [Strands Agents](https://github.com/strands-agents/sdk-python) | [RenderCV](https://rendercv.com)

**License:** MIT | [Issues & PRs](https://github.com/cagataycali/strands-rendercv)
