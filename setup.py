from setuptools import setup, find_packages


install_requirement_list = [
    'opencv-python',
    'imutils',
    'numpy',
    'loguru',
    'opencv-contrib-python==3.4.2.17',
    'scikit-learn',
    'scikit-image',
    'flask',
    'gevent',
    'scipy',
]

setup(
    name='hyper-find',
    version='1.0.0',
    description='find target icon on your picture, hyper ui test',
    author='yanzongzhen',
    author_email='yanzongzhen127@outlook.com',
    url='https://github.com/yanzongzhen/hyper-find',
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=install_requirement_list
)
