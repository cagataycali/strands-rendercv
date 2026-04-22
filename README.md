# strands-rendercv

[![PyPI version](https://badge.fury.io/py/strands-rendercv.svg)](https://pypi.org/project/strands-rendercv/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

[![Awesome Strands Agents](https://img.shields.io/badge/Awesome-Strands%20Agents-00FF77?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkwIiBoZWlnaHQ9IjQ2MyIgdmlld0JveD0iMCAwIDI5MCA0NjMiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxwYXRoIGQ9Ik05Ny4yOTAyIDUyLjc4ODRDODUuMDY3NCA0OS4xNjY3IDcyLjIyMzQgNTYuMTM4OSA2OC42MDE3IDY4LjM2MTZDNjQuOTgwMSA4MC41ODQzIDcxLjk1MjQgOTMuNDI4MyA4NC4xNzQ5IDk3LjA1MDFMMjM1LjExNyAxMzkuNzc1QzI0NS4yMjMgMTQyLjc2OSAyNDYuMzU3IDE1Ni42MjggMjM2Ljg3NCAxNjEuMjI2TDMyLjU0NiAyNjAuMjkxQy0xNC45NDM5IDI4My4zMTYgLTkuMTYxMDcgMzUyLjc0IDQxLjQ4MzUgMzY3LjU5MUwxODkuNTUxIDQxMS4wMDlMMTkwLjEyNSA0MTEuMTY5QzIwMi4xODMgNDE0LjM3NiAyMTQuNjY1IDQwNy4zOTYgMjE4LjE5NiAzOTUuMzU1QzIyMS43ODQgMzgzLjEyMiAyMTQuNzc0IDM3MC4yOTYgMjAyLjU0MSAzNjYuNzA5TDU0LjQ3MzggMzIzLjI5MUM0NC4zNDQ3IDMyMC4zMjEgNDMuMTg3OSAzMDYuNDM2IDUyLjY4NTcgMzAxLjgzMUwyNTcuMDE0IDIwMi43NjZDMzA0LjQzMiAxNzkuNzc2IDI5OC43NTggMTEwLjQ4MyAyNDguMjMzIDk1LjUxMkw5Ny4yOTAyIDUyLjc4ODRaIiBmaWxsPSIjRkZGRkZGIi8+CjxwYXRoIGQ9Ik0yNTkuMTQ3IDAuOTgxODEyQzI3MS4zODkgLTIuNTc0OTggMjg0LjE5NyA0LjQ2NTcxIDI4Ny43NTQgMTYuNzA3NEMyOTEuMzExIDI4Ljk0OTIgMjg0LjI3IDQxLjc1NyAyNzIuMDI4IDQ1LjMxMzhMNzEuMTcyNyAxMDMuNjcxQzQwLjcxNDIgMTEyLjUyMSAzNy4xOTc2IDE1NC4yNjIgNjUuNzQ1OSAxNjguMDgzTDI0MS4zNDMgMjUzLjA5M0MzMDcuODcyIDI4NS4zMDIgMjk5Ljc5NCAzODIuNTQ2IDIyOC44NjIgNDAzLjMzNkwzMC40MDQxIDQ2MS41MDJDMTguMTcwNyA0NjUuMDg4IDUuMzQ3MDggNDU4LjA3OCAxLjc2MTUzIDQ0NS44NDRDLTEuODIzOSA0MzMuNjExIDUuMTg2MzcgNDIwLjc4NyAxNy40MTk3IDQxNy4yMDJMMjE1Ljg3OCAzNTkuMDM1QzI0Ni4yNzcgMzUwLjEyNSAyNDkuNzM5IDMwOC40NDkgMjIxLjIyNiAyOTQuNjQ1TDQ1LjYyOTcgMjA5LjYzNUMtMjAuOTgzNCAxNzcuMzg2IC0xMi43NzcyIDc5Ljk4OTMgNTguMjkyOCA1OS4zNDAyTDI1OS4xNDcgMC45ODE4MTJaIiBmaWxsPSIjRkZGRkZGIi8+Cjwvc3ZnPgo=&logoColor=white)](https://github.com/cagataycali/awesome-strands-agents)

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
