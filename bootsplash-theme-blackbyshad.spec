
%define		theme	blackbyshad

Summary:	Bootsplash - PLD black by shad theme
Summary(de):	Bootsplash - PLD black by shad Thema f�r Bootsplash
Summary(pl):	Bootsplash - motyw PLD dark black wg shada
Name:		bootsplash-theme-%{theme}
Version:	1.0
Release:	1
Epoch:		0
License:	GPL v2
Group:		Themes
Source0:	http://www.atwa.us/~shadzik/bootsplash-theme-pldblackbyshad-%{version}.tar.bz2
# Source0-md5:	7efd0cc598c71ba73b6534569ebe2253
URL:		http://www.atwa.us/~shadzik/pldblackbyshad.tar.bz2
Requires:	bootsplash
Obsoletes:	bootsplash-theme-pldblackbyshad
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD black theme by shad for bootsplash.

%description -l de
PLD black by shad Thema f�r Bootsplash.

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
