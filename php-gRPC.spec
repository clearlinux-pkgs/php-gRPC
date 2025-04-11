#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : php-gRPC
Version  : 1.71.0
Release  : 103
URL      : https://pecl.php.net/get/grpc-1.71.0.tgz
Source0  : https://pecl.php.net/get/grpc-1.71.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: php-gRPC-lib = %{version}-%{release}
Requires: php-gRPC-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : file
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Overview
This directory contains source code for PHP implementation of gRPC layered on
shared C library. The same installation guides with more examples and
tutorials can be seen at [grpc.io](https://grpc.io/docs/languages/php/quickstart).
gRPC PHP installation instructions for Google Cloud Platform is in
[cloud.google.com](https://cloud.google.com/php/grpc).

%package lib
Summary: lib components for the php-gRPC package.
Group: Libraries
Requires: php-gRPC-license = %{version}-%{release}

%description lib
lib components for the php-gRPC package.


%package license
Summary: license components for the php-gRPC package.
Group: Default

%description license
license components for the php-gRPC package.


%prep
%setup -q -n grpc-1.71.0
cd %{_builddir}/grpc-1.71.0
pushd ..
cp -a grpc-1.71.0 buildavx2
popd

%build
## build_prepend content
export GCC_IGNORE_WERROR=1
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-gRPC
cp %{_builddir}/grpc-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-gRPC/242ec6abfdd8c114f2e803b84934469c299348fc || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20240924/grpc.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-gRPC/242ec6abfdd8c114f2e803b84934469c299348fc
