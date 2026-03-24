

# Slot: id 


_疾病的唯一識別碼 (例如 MONDO ID)_





URI: [https://w3id.org/my-github/disease-model/id](https://w3id.org/my-github/disease-model/id)
Alias: id

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
| Identifier | Yes |
| Owner | [Disease](Disease.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/my-github/disease-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/my-github/disease-model/id |
| native | https://w3id.org/my-github/disease-model/id |




## LinkML Source

<details>
```yaml
name: id
description: 疾病的唯一識別碼 (例如 MONDO ID)
from_schema: https://w3id.org/my-github/disease-model
rank: 1000
identifier: true
alias: id
owner: Disease
domain_of:
- Disease
range: string
required: true

```
</details>