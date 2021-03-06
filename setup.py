import os
from setuptools import setup, find_packages
PACKAGES = find_packages()

# Get version and release info, which is all stored in shablona/version.py
ver_file = os.path.join('nitools', 'version.py')

with open(ver_file) as f:
    exec(f.read())

# Long description will go up on the pypi page
with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

with open('requirements.txt') as f:
    REQUIRES = f.readlines()

opts = dict(name=NAME,
            maintainer=MAINTAINER,
            maintainer_email=MAINTAINER_EMAIL,
            description=DESCRIPTION,
            long_description=LONG_DESCRIPTION,
            url=URL,
            download_url=DOWNLOAD_URL,
            license=LICENSE,
            classifiers=CLASSIFIERS,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            platforms=PLATFORMS,
            version=VERSION,
            packages=PACKAGES,
            package_data=PACKAGE_DATA,
            install_requires=REQUIRES,
            requires=REQUIRES,
            scripts=['bin/fslvbm_2_template_fmriprep', 'bin/fslvbm_3_proc_fmriprep'],
            entry_points={
                'console_scripts': [
                    'start_nitools = nitools.cmd_tools:start_nitools',
                    'run_qc_and_preproc = nitools.cmd_tools:run_qc_and_preproc',
                    'run_qc = nitools.qc:run_qc_cmd',
                    'run_preproc = nitools.preproc:run_preproc_cmd',
                    'scale_MP2RAGE = nitools.utils:scale_MP2RAGE',
                    'compute_TSNR = nitools.utils:compute_TSNR'
                    ]
                }
            )

if __name__ == '__main__':
    setup(**opts)
