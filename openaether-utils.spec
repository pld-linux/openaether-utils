%define _snap 20040713

Summary:	Misc jabber utilities
Summary(pl):	Ró¿ne narzêdzie jabberowe
Name:		openaether-utils
Version:	%{_snap}
Release:	0.1
#TODO: check this
License:	GPL
Group:		Libraries
Source0:	http://www.lukasz.mach.com.pl/oa-utils-%{version}.tar.bz2
# Source0-md5:	46098c43a8acf71c0368a45b09ba2e20
Patch0:		%{name}-oapr_includes.patch
BuildRequires:	oapr-devel
BuildRequires:	apr-util-devel
BuildRequires:	oajabber-devel
BuildRequires:	xerces-c-devel
BuildRequires:	zlib-devel
BuildRequires:	boost-conversion-devel
BuildRequires:	boost-python-devel
URL:		http://gen.openaether.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of misc programs using oajabber library

%description -l pl
Kolekcja ró¿nych programów u¿ywaj±cych biblioteki oajabber

%prep
%setup -q -n oa-utils-%{_snap}
%patch0 -p0

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure --disable-bootstrap --with-apr=%{_bindir} --with-apu=%{_bindir} 	--with-oapu=%{_bindir}

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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_bindir}/jab*
