Summary:	View and compare your fonts
Summary(pl.UTF-8):   Narzędzie do oglądania i porównywania fontów
Name:		gfontsampler
Version:	0.4
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://linuxadvocate.org/projects/gfontsampler/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	db2dadf22192861475686030a17c300e
Patch0:		%{name}-desktop.patch
URL:		http://linuxadvocate.org/projects/gfontsampler/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.14.3
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
View and compare your fonts.

%description -l pl.UTF-8
Narzędzie do oglądania i porównywania fontów.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake} 
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}/%{name}-icon.png \
    $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
mv -f $RPM_BUILD_ROOT%{_datadir}/gnome/apps/Utilities/* \
	$RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/gfontsampler
%{_datadir}/%{name}
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/%{name}.desktop
