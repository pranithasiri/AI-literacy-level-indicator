def generate_curriculum(report):

    tech = report.get("technical_understanding_percent", {})
    prac = report.get("practical_application_percent", {})
    crit = report.get("critical_appraisal_percent", {})

    tech_low = tech.get("Low", 0)
    prac_low = prac.get("Low", 0)
    crit_low = crit.get("Low", 0)

    curriculum = []

    if tech_low > 30:
        curriculum.append({
            "module": "Technical Foundations of AI",
            "topics": [
                "How AI models work",
                "Machine learning basics",
                "Understanding AI systems"
            ],
            "duration": "4 weeks"
        })

    if prac_low > 30:
        curriculum.append({
            "module": "Practical AI Usage",
            "topics": [
                "Prompt engineering",
                "Using AI tools effectively",
                "AI productivity workflows"
            ],
            "duration": "3 weeks"
        })

    if crit_low > 30:
        curriculum.append({
            "module": "Critical AI Literacy",
            "topics": [
                "AI bias",
                "AI hallucinations",
                "Evaluating AI output"
            ],
            "duration": "3 weeks"
        })

    return curriculum