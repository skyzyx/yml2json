# Known Issues
## Single-bang tags

In <http://www.yaml.org/spec/1.2/spec.html>, it lists a new document with a `!` tag.

```yaml
--- !<tag:clarkevans.com,2002:invoice>
```

This is not supported by PyYAML, and therefore not supported by `yml2json`. Instead, you need to remove the `!` tag.

In simple cases, you can remove this by hand, leaving only the document-start annotation: `---`.

In more complex cases, you can use regular expressions (e.g., PCRE) to find matches, then replace them with `---`.

```
^---\s+!<([^>]*)>\s*$
```

## Single-bang elements

In <http://www.yaml.org/spec/1.2/spec.html>, it lists the single-bang element, `!local`.

```yaml
%YAML 1.2
---
!!map {
  ? !!str "anchored"
  : !local &A1 "value",
  ? !!str "alias"
  : *A1,
}
```

This is the same example with inferred types:

```yaml
anchored: !local &anchor value
alias: *anchor
```

This is not supported by PyYAML, and therefore not supported by `yml2json`.

## Colons must be quoted

If you have a string which contains a `:` character (e.g., URI schemes), then you must explicitly quote it as a string, otherwise PyYAML will choke.

## JSON maps for keys

Although YAML 1.2 defines all JSON objects as valid YAML objects, PyYAML only supports YAML 1.1. This also means that using maps for keys does not work here.
