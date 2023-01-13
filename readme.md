# Yaml Bomb

Yaml bomb files and exploitable programming languages

## What is a bomb?

A bomb is a special type of payload usually targeted at web servers with internet-facing endpoints that upon serialization expands in size on an exponential scale, taking up all the available memory of the systems and eventually crashing them. These crashes cause outages, so bombs are ideal for denial-of-service attacks.

## How does the Yaml bomb work?

Like in many cases with other bombs, a feature of a serialization format to replicate content is used. This way we can embed more data in a smaller space. YAML supports declaring variables. 

```yaml
firstLink: &example 'https://example.com'
links:
  - *example
  - https://example.com/fake
```

These variables are useful to repeat data in multiple places. For example in a configuration file use-case, this would mean that some data only have to be changed in one place. The previous YAML would evaluate to the following file:

```yaml
firstLink: 'https://example.com'
links:
  - 'https://example.com'
  - 'https://example.com/fake'
```

Since data can be multiplied this way, nothing stops us from declaring something, and using it to declare something else

```yaml
apple: &one apples
apples: &five [ *one,*one,*one,*one,*one ]
appless: &twentyfive [ *five,*five,*five,*five,*five ]
...
```

Repeating steps like these and making the repeating part less verbose yields the results visible in the files:

- `bomb.small.yaml`
- `bomb.pb.yaml`

## Size

|Lines|Packed Data|Unpacked Data|Scaling factor|
|-|-|-|-|
|1|37 B|82.0 B|2x|
|2|74 B|859.0 B|11x|
|3|111 B|8.48 KB|78x|
|4|148 B|83.8 KB|579x|
|5|185 B|837.93 KB|4,638x|
|6|222 B|8.18 MB|38,649x|
|7|259 B|81.83 MB|331,284x|
|8|296 B|818.28 MB|2,898,738x|
|9|333 B|7.99 GB|25,766,567x|
|10|370 B|79.91 GB|231,899,108x|
|11|407 B|799.1 GB|2,108,173,710x|
|12|444 B|7.8 TB|19,324,925,675x|
|13|481 B|78.04 TB|178,383,929,313x|
|14|518 B|780.37 TB|1,656,422,200,772x|
|15|555 B|7.62 PB|15,459,940,540,540x|

# Vulnerable package

- **Python PyYAML**: parses until crashes
- **NodeJS YAML**: Crashes with error: "_ReferenceError: Excessive alias count indicates a resource exhaustion attack_"
- **Python JS-YAML**: parses until crashes
