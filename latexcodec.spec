#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : latexcodec
Version  : 2.0.1
Release  : 16
URL      : https://files.pythonhosted.org/packages/84/2f/fd47712130b303ff179c819cc5c63aa39586fc8d430bc299c0f5f56ec42c/latexcodec-2.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/84/2f/fd47712130b303ff179c819cc5c63aa39586fc8d430bc299c0f5f56ec42c/latexcodec-2.0.1.tar.gz
Summary  : A lexer and codec to work with LaTeX code in Python.
Group    : Development/Tools
License  : MIT
Requires: latexcodec-license = %{version}-%{release}
Requires: latexcodec-python = %{version}-%{release}
Requires: latexcodec-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(six)

%description
latexcodec
==========
|travis| |codecov|
A lexer and codec to work with LaTeX code in Python.

%package license
Summary: license components for the latexcodec package.
Group: Default

%description license
license components for the latexcodec package.


%package python
Summary: python components for the latexcodec package.
Group: Default
Requires: latexcodec-python3 = %{version}-%{release}

%description python
python components for the latexcodec package.


%package python3
Summary: python3 components for the latexcodec package.
Group: Default
Requires: python3-core
Provides: pypi(latexcodec)
Requires: pypi(six)

%description python3
python3 components for the latexcodec package.


%prep
%setup -q -n latexcodec-2.0.1
cd %{_builddir}/latexcodec-2.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637346987
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/latexcodec
cp %{_builddir}/latexcodec-2.0.1/LICENSE.rst %{buildroot}/usr/share/package-licenses/latexcodec/c6ae10266f790496c89892ab3edd10966c80ffdb
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/latexcodec/c6ae10266f790496c89892ab3edd10966c80ffdb

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
