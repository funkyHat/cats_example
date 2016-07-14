from setuptools import setup

# Replace the place holders with values for your project

setup(

    # Do not use underscores in the plugin name.
    name='cat_rescue',

    version='0.1',

    # This must correspond to the actual packages in the plugin.
    py_modules=[
        'owner',
    ],

    install_requires=[
        'factory_boy',
    ],
)
