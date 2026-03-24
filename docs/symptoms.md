

# Slot: symptoms 


_該疾病對應的表型 ID (HPO ID)_





URI: [https://w3id.org/my-github/disease-model/symptoms](https://w3id.org/my-github/disease-model/symptoms)
Alias: symptoms

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Disease](Disease.md) | 表示一種疾病實體 |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Disease](Disease.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Disease](Disease.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/my-github/disease-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/my-github/disease-model/symptoms |
| native | https://w3id.org/my-github/disease-model/symptoms |




## LinkML Source

<details>
```yaml
name: symptoms
description: 該疾病對應的表型 ID (HPO ID)
from_schema: https://w3id.org/my-github/disease-model
rank: 1000
alias: symptoms
owner: Disease
domain_of:
- Disease
range: string
multivalued: true

```
</details>