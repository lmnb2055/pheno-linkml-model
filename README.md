# pheno-linkml-model (Sandbox)

This repository is a technical demonstration of using **LinkML** to create a standardized, machine-readable data model for disease-phenotype associations.

## Project Goals
- Implement a **Schema-First** approach to biomedical data modeling.
- Ensure data integrity using **LinkML Validation**.
- Map local attributes to global standards (e.g., **MONDO**, **HPO**).
- Explore automated artifact generation (Python, JSON Schema, Markdown).

## Tech Stack
- **Modeling:** LinkML (YAML)
- **Validation:** LinkML-Validator
- **Ontologies:** MONDO (Diseases), HPO (Phenotypes)
- **Language:** Python 3.12+

## Current Progress
- [x] Basic LinkML schema defined.
- [x] Python Data Classes auto-generated via `gen-python`.
- [x] Successful validation of JSON payloads.
- [ ] *Next Step: Exporting validated data to KGX format.*
