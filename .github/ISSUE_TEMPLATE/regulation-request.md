---
name: Regulation Request
about: Add compliance rules for a country or law
title: "[Regulation] "
labels: regulation
body:
  - type: input
    id: jurisdiction
    attributes:
      label: Jurisdiction (ISO code)
      placeholder: IN, EU, US
    validations:
      required: true
  - type: input
    id: law_name
    attributes:
      label: Law / Regulation name
    validations:
      required: true
  - type: input
    id: source_url
    attributes:
      label: Official source URL
    validations:
      required: true
  - type: textarea
    id: summary
    attributes:
      label: Why is this regulation important?
