from setuptools import setup

REQUIREMENTS = ['scipy', 'numpy','pandas', 'scikit-learn', 'torch', 'matplotlib', 'pyteomics', 'pymzml', 'networkx']

setup(
    name='BLINK',
    version='1.1',
    description='Package for efficiently generating cosine-based similarity scores and matching ion counts for large numbers of fragmentation mass spectra',
    author='Neus Pou Amengual',
    author_email='np@olobion.ai',
    url='https://github.com/oloBion/blink',
    install_requires = REQUIREMENTS,
    packages = ['blink'],
    python_requires='>=3.10',
    py_modules=['blink', 'blink_cli', 'data_binning', 'matrix_manipulation',
                'msn_io', 'scoring', 'spectral_normalization', 'utils']
    )