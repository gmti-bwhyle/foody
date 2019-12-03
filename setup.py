from setuptools import setup, find_packages
import sam

if __name__ == '__main__':
	setup(
		name='sam',
		version=sam.__version__,
		description="GDP Subscription and Account Management",
		long_description="""""",
		classifiers=['License :: Other/Proprietary License'],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
		author='Gannett',
		url='',
		zip_safe=False,
		include_package_data=True,
		packages=find_packages(),
		provides=find_packages(include=['sam']),
		setup_requires=(
			"wheel",
			"a-tools"
		),
		install_requires=(
			"python-memcached==1.53",
			"Django==1.6.5",
			"pystache==0.5.4",
			"slimit==0.7.4",
			"cssutils==0.9.10",
			"cssmin==0.1.4",
			"firefly-core==1.6.1",
			"gannett-utilities<1.0.0",
			"mock==1.3.0",
			"pytz==2013.8",
			"ply==3.4",  # A dependency for slimit. Must be 3.4 or SAM will break.
			'ui-service-framework>=5.2.0,<6.0.0',
			"vcrpy==1.11.1", # A dependency for stubbing
		)
	)
