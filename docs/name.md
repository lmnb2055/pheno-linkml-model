

# Slot: name 


_疾病名稱_





URI: [https://w3id.org/my-github/disease-model/name](https://w3id.org/my-github/disease-model/name)
Alias: name

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
| Required | Yes |
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
| self | https://w3id.org/my-github/disease-model/name |
| native | https://w3id.org/my-github/disease-model/name |




## LinkML Source

<details>
```yaml
name: name
description: 疾病名稱
from_schema: https://w3id.org/my-github/disease-model
rank: 1000
alias: name
owner: Disease
domain_of:
- Disease
range: string
required: true

```
</details>