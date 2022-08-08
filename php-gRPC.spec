#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-gRPC
Version  : 1.47.0
Release  : 28
URL      : https://pecl.php.net/get/grpc-1.47.0.tgz
Source0  : https://pecl.php.net/get/grpc-1.47.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: php-gRPC-lib = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : pkgconfig(zlib)

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

%description lib
lib components for the php-gRPC package.


%prep
%setup -q -n grpc-1.47.0
cd %{_builddir}/grpc-1.47.0

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
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/grpc.so
