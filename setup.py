from setuptools import setup, find_packages

setup(name='ninfo-plugin-shodan',
    version='0.1.2',
    zip_safe=False,
    packages = find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        "ninfo>=0.1.11",
        "shodan",
        "simplejson",
    ],
    entry_points = {
        'ninfo.plugin': [
            'shodan      = ninfo_plugin_shodan',
        ]
    }
) 
