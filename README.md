# JSON schema for research metadata at ZMT

This repository will hold the [JSON schema](https://json-schema.org) for metadata to be used for research data at ZMT. A schema defines the structure and allowed types and values for metadata (see <https://json-schema.org/understanding-json-schema/about.html> for "What is a schema?"). 

The JSON schema is a well-established format for schemas that allows validation of the metadata in many contexts (see <https://json-schema.org/implementations.html>). It is also possible to use the [Polyglottal JSON Schema Validator](https://github.com/json-schema-everywhere/pajv) to validate other languages such as YAML and TOML. For example, metadata placed inside a [research data folder](https://gitlab.leibniz-zmt.de/digiz/database/data-folder-structure) can be checked for errors and missing entries.

As the data publisher PANGAEA is the main endpoint of ZMT's research data this schema will be developed to be compatible with [PANAGAEA's data model](https://wiki.pangaea.de/wiki/Data_model) for projects, staff members, events, datasets etc (see also the [PANGAEA XML schema](https://wiki.pangaea.de/wiki/PANGAEA_XML_schema), with additional ZMT-specific information.
