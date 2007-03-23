
%define		theme	blackbyshad

Summary:	Bootsplash - PLD black by shad theme
Summary(de):	Bootsplash - PLD black by shad Thema für Bootsplash
Summary(pl):	Bootsplash - motyw PLD dark black wg shada
Name:		bootsplash-theme-%{theme}
Version:	1.0
Release:	1
Epoch:		0
License:	GPL v2
Group:		Themes
Source0:	http://shadzik.atwa.us/content/%{theme}/%{name}-%{version}.tar.bz2
# Source0-md5:	70057d955f55fbee8a71e479765048cb
URL:		http://www.atwa.us/~shadzik/content/blackbyshad/
Requires:	bootsplash
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD black theme by shad for bootsplash.

%description -l de
PLD black by shad Thema für Bootsplash.

%description -l pl
Motyw PLD black do bootsplash wg. shada.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
THEME_DIR=$RPM_BUILD_ROOT%{_sysconfdir}/bootsplash/themes/%{theme}
install -d $THEME_DIR/{config,images}
install %{theme}/config/*.cfg $THEME_DIR/config
install %{theme}/images/*.jpg $THEME_DIR/images

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/bootsplash/themes/%{theme}
