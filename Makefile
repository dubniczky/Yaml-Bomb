# Test python
python::
	@python ./python/main.py bomb.small.yaml

# Test nodejs yaml package
nodejs_yaml::
	@node nodejs/yaml/main.js bomb.small.yaml

# Test nodejs yaml package
nodejs_js-yaml::
	@node nodejs/js-yaml/main.js bomb.small.yaml
