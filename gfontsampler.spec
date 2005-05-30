Summary:	View and compare your fonts
Summary(pl):	Zobacz i porównaj swoje czcionki
Name:		gfontsampler
Version:	0.4
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://linuxadvocate.org/projects/gfontsampler/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	db2dadf22192861475686030a17c300e
Source1:	%{name}.desktop
URL:		http://linuxadvocate.org/projects/gfontsampler/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	libgnomeui-devel
BuildRequires:	popt-devel
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
View and compare your fonts.

%description -l pl
Zobacz i porównaj swoje czcionki.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
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

install %{SOURCE1} $RPM_BUILD_ROOT/%{_desktopdir}

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/gfontsampler
%{_datadir}/%{name}/glade/*.glade
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/%{name}.desktop
