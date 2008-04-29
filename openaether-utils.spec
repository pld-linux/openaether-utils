%define _snap 20040713

Summary:	Misc jabber utilities
Summary(pl.UTF-8):	Różne narzędzie jabberowe
Name:		openaether-utils
Version:	%{_snap}
Release:	0.1
#TODO: check this
License:	GPL
Group:		Libraries
Source0:	oa-utils-%{version}.tar.bz2
# Source0-md5:	46098c43a8acf71c0368a45b09ba2e20
Patch0:		%{name}-oapr_includes.patch
URL:		http://gen.openaether.org/
BuildRequires:	apr-util-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	boost-python-devel
BuildRequires:	libtool
BuildRequires:	oajabber-devel
BuildRequires:	oapr-devel
BuildRequires:	xerces-c-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of misc programs using oajabber library.

%description -l pl.UTF-8
Kolekcja różnych programów używających biblioteki oajabber.

%prep
%setup -q -n oa-utils-%{_snap}
%patch0 -p0

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-bootstrap \
	--with-apr=%{_bindir} \
	--with-apu=%{_bindir} \
	--with-oapu=%{_bindir}

%{__make} \
	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/jab*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
