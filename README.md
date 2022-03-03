# JSON schema for research metadata at ZMT

This repository contains the metadata schemas as [JSON schema](https://json-schema.org) to be used for research data at ZMT. A schema defines the structure and allowed types and values for metadata (see <https://json-schema.org/understanding-json-schema/about.html> for "What is a schema?"). 

The JSON schema is a well-established format for schemas that allows validation of the metadata in many contexts (see <https://json-schema.org/implementations.html>). It is also possible to use the [Polyglottal JSON Schema Validator](https://github.com/json-schema-everywhere/pajv) to validate other languages such as YAML and TOML. For example, the schema for a [Dataset](schemas/dataset.schema.json) is used to define the metadata input form in the [Nextcloud Metadata Editor](https://github.com/leibniz-zmt/files_metadataeditor) app and the data model of [ZMT's Research Database](https://data.zmt-datalab.de).

As the data publisher PANGAEA is the main endpoint of ZMT's research data this schema is supposed to be largely compatible with [PANAGAEA's data model](https://wiki.pangaea.de/wiki/Data_model) for projects, staff members, events, datasets etc (see also the [PANGAEA XML schema](https://wiki.pangaea.de/wiki/PANGAEA_XML_schema).
