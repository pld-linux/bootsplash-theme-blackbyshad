
%define		theme	blackbyshad

Summary:	Bootsplash - PLD black by shad theme
Summary(de.UTF-8):	Bootsplash - PLD black by shad Thema für Bootsplash
Summary(pl.UTF-8):	Bootsplash - motyw PLD dark black wg shada
Name:		bootsplash-theme-%{theme}
Version:	1.1
Release:	1
Epoch:		0
License:	GPL v2
Group:		Themes
Source0:	http://shadzik.atwa.us/content/blackbyshad/%{name}-%{version}.tar.bz2
# Source0-md5:	2b5993925498541e08d7385aad4d1a39
URL:		http://www.atwa.us/~shadzik/content/blackbyshad/
Requires:	bootsplash
Provides:	bootsplash-theme
Obsoletes:	bootsplash-theme-pldblackbyshad
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD black theme by shad for bootsplash.

%description -l de.UTF-8
PLD black by shad Thema für Bootsplash.

%description -l pl.UTF-8
Motyw PLD black do bootsplash wg shada.

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
