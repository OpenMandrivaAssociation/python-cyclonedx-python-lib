Name:		python-cyclonedx-python-lib
Version:	11.1.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/c/cyclonedx-python-lib/cyclonedx_python_lib-%{version}.tar.gz
Summary:	Python library for CycloneDX
URL:		https://pypi.org/project/cyclonedx-python-lib/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python
BuildRequires:  python%{pyver}dist(poetry-core)
BuildSystem:	python
BuildArch:	noarch

%description
Python library for CycloneDX

%files
%{py_sitedir}/cyclonedx
%{py_sitedir}/cyclonedx_python_lib-*.*-info
