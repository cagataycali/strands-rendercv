# CV Examples

This directory contains realistic, detailed CV examples showcasing different roles, themes, and use cases for strands-rendercv.

## Available Examples

### 1. Senior Software Engineer ([senior_swe_cv.yaml](senior_swe_cv.yaml))
**Theme:** `engineeringresumes` (dense, engineering-focused)

**Profile:** Alex Chen - 8 years experience in distributed systems
- **Companies:** AWS, Google, Microsoft, Dropbox
- **Skills:** Distributed systems, cloud architecture, system design
- **Highlights:** Publications, open source projects, conference talks
- **Sections:** Summary, work experience, education, projects, publications, skills, awards

**Use for:** Software engineering roles at FAANG, distributed systems, cloud infrastructure

### 2. ML Researcher ([ml_researcher_cv.yaml](ml_researcher_cv.yaml))
**Theme:** `classic` (clean professional)

**Profile:** Dr. Maya Patel - PhD in CS, postdoc at Stanford AI Lab
- **Research:** Foundation models, multimodal learning, AI alignment
- **Publications:** 6 top-tier papers (NeurIPS, ICML, CVPR, ICLR)
- **Experience:** Stanford, OpenAI, Google Brain
- **Highlights:** 2500+ citations, NSF grant, best paper awards
- **Sections:** Summary, work experience, education, publications, skills, awards

**Use for:** Academic positions, research scientist roles, AI/ML research

### 3. Product Designer ([product_designer_cv.yaml](product_designer_cv.yaml))
**Theme:** `moderncv` (contemporary with color)

**Profile:** Jordan Rivera - 6 years in product design
- **Companies:** Stripe, Airbnb, Spotify
- **Skills:** Design systems, user research, accessibility
- **Highlights:** Open source design system, WCAG compliance, Webby Award
- **Sections:** Summary, work experience, education, projects, skills, awards

**Use for:** Product design, UX/UI design, design systems roles

### 4. Startup Founder ([startup_founder_cv.yaml](startup_founder_cv.yaml))
**Theme:** `sb2nov` (modern single-column)

**Profile:** Marcus Thompson - Serial entrepreneur, 2 successful exits
- **Exits:** CodeMesh (45M USD to GitLab), APIHub (40M USD to MuleSoft)
- **Current:** Building DevFlow AI (8M USD seed from a16z)
- **Skills:** Fundraising, growth strategy, team building, technical leadership
- **Highlights:** 85M USD total exits, Forbes 30 Under 30, angel investor
- **Sections:** Summary, work experience, education, awards

**Use for:** Executive roles, founder positions, entrepreneurial roles

### 5. Developer Advocate ([devrel_engineer_cv.yaml](devrel_engineer_cv.yaml))
**Theme:** `engineeringresumes` (engineering-focused)

**Profile:** Priya Sharma - 7 years in developer relations
- **Companies:** AWS, Google Cloud, Microsoft
- **Skills:** Community building, content creation, technical speaking
- **Content:** 50K YouTube subscribers, 200+ articles, podcast host
- **Highlights:** 80+ conference talks, 3 open source projects, AWS re:Invent keynote
- **Sections:** Summary, work experience, education, content/community, skills, awards

**Use for:** Developer advocate, developer relations, technical community roles

---

## How to Use Examples

### 1. Generate a CV from an example

```python
from strands import Agent
from strands_rendercv import render_cv

agent = Agent(
    model="us.anthropic.claude-sonnet-4-20250514-v1:0",
    tools=[render_cv]
)

# Generate Senior SWE CV
agent.tool.render_cv(
    action="render",
    input_file="examples/senior_swe_cv.yaml"
)
```

### 2. Validate an example

```python
agent.tool.render_cv(
    action="validate",
    input_file="examples/ml_researcher_cv.yaml"
)
```

### 3. Use as template

```bash
# Copy an example as starting point
cp examples/product_designer_cv.yaml my_cv.yaml

# Edit with your information
vim my_cv.yaml

# Generate your CV
python -c "
from strands import Agent
from strands_rendercv import render_cv
agent = Agent(tools=[render_cv])
agent.tool.render_cv(action='render', input_file='my_cv.yaml')
"
```

### 4. Compare themes

Generate the same content with different themes:

```python
# Try all themes
themes = ["engineeringresumes", "classic", "sb2nov", "moderncv", "engineeringclassic"]

for theme in themes:
    agent.tool.render_cv(
        action="render",
        input_file="examples/senior_swe_cv.yaml",
        overrides=f'{{"design.theme": "{theme}"}}',
        output_dir=f"./output/{theme}"
    )
```

---

## Example Features Showcase

### All Examples Include

| Feature | All Examples | Notes |
|---------|--------------|-------|
| **Detailed work experience** | ✅ | 4-8 roles with 4-7 highlights each |
| **Education** | ✅ | Degrees with GPA and achievements |
| **Skills** | ✅ | Categorized by domain |
| **Contact info** | ✅ | Email, phone, website, social networks |
| **Clean formatting** | ✅ | No special characters (%, #, π) |
| **Proper date format** | ✅ | YYYY-MM or "present" |

### Unique Features

| Feature | Examples |
|---------|----------|
| **Publications** | ML Researcher, Senior SWE |
| **Projects** | Senior SWE, Product Designer |
| **Content/Community** | DevRel Engineer |
| **Angel Investing** | Startup Founder |
| **Awards section** | All examples |
| **Multiple social networks** | All examples |
| **Phone number** | 4 out of 5 (optional field) |

---

## Customization Tips

### Change Theme
```yaml
design:
  theme: engineeringresumes  # or classic, sb2nov, moderncv, engineeringclassic
```

### Change Color (moderncv and sb2nov)
```yaml
design:
  color: rgb(50,50,150)  # Blue
  # or
  color: rgb(144,79,0)   # Orange
```

### Add Your Own Section
```yaml
cv:
  sections:
    # ... other sections ...
    
    certifications:
      - label: AWS Certifications
        details: "Solutions Architect Professional, DevOps Engineer Professional"
      
      - label: Other Certifications
        details: "CKA, CKAD, Terraform Associate"
```

### Customize Highlights Format
```yaml
work_experience:
  - company: Your Company
    position: Your Role
    start_date: 2020-01
    end_date: present
    highlights:
      - "Led team of 5 engineers building X feature"
      - "Improved performance by 40 percent through optimization"
      - "Reduced costs by 2M USD annually"
```

---

## AI-Powered Customization

Use Strands Agents to customize examples:

```python
agent("""
Read the senior_swe_cv.yaml example.
Adapt it for a Staff Engineer role at Google focusing on:
- Infrastructure and platform engineering
- Technical leadership and mentorship
- Large-scale distributed systems

Generate a new YAML file called my_staff_cv.yaml
""")
```

---

## Validation Checklist

Before generating your CV, validate:

1. ✅ **Required:** `cv.name` exists
2. ✅ **Sections:** Under `cv.sections:`, not root level
3. ✅ **Dates:** Format `YYYY-MM` or `YYYY-MM-DD` or `present`
4. ✅ **Phone:** Format `+1 234 567 8900` (if included)
5. ✅ **URLs:** Valid URL format
6. ✅ **Special chars:** No `#`, `%`, `π` symbols
7. ✅ **Theme:** One of 5 valid themes

Run validation:
```python
agent.tool.render_cv(action="validate", input_file="your_cv.yaml")
```

---

## Example Metrics

| Metric | Senior SWE | ML Researcher | Product Designer | Startup Founder | DevRel |
|--------|-----------|---------------|------------------|-----------------|--------|
| **Pages** | 2-3 | 3-4 | 2 | 2 | 2-3 |
| **Work roles** | 4 | 3 | 3 | 4 | 3 |
| **Education** | 1 degree | 2 degrees | 1 degree | 2 degrees | 1 degree |
| **Projects** | 3 | 0 | 3 | 0 | 0 |
| **Publications** | 2 | 6 | 0 | 0 | 0 |
| **Skills sections** | 6 | 5 | 6 | 5 | 6 |
| **Awards section** | Yes | Yes | Yes | Yes | Yes |
| **Content section** | No | No | No | No | Yes |

---

## Common Use Cases

### Use Case 1: Career Change
Start with similar role example → Adapt sections → Add transitional skills

```python
agent("""
Read product_designer_cv.yaml.
Adapt it for someone transitioning from design to product management.
Focus on: stakeholder management, data-driven decisions, cross-functional leadership.
""")
```

### Use Case 2: Different Seniority
Start with any example → Adjust experience length → Remove/add sections

**Junior:** Remove publications, reduce projects, focus on education and internships
**Mid-level:** 3-5 years experience, some projects, growing skills
**Senior/Staff:** Leadership focus, mentorship, technical depth, publications

### Use Case 3: Industry Change
Keep structure → Replace companies → Adapt highlights → Adjust skills

**Tech → Finance:** Same engineering skills + add: risk management, compliance, fintech
**Startup → Enterprise:** Same skills + add: stakeholder management, process, scale

---

## Further Resources

- [RenderCV Documentation](https://docs.rendercv.com)
- [Main README](../README.md)
- [YAML Schema](https://docs.rendercv.com/user_guide/structure_of_the_yaml_input_file/)

---

**Questions?** Open an issue at [github.com/cagataycali/strands-rendercv](https://github.com/cagataycali/strands-rendercv)
