
%define		theme	xmmsbar

Summary:	superkaramba - xmmsbar theme
Summary(pl):	superkaramba - motyw xmmsbar
Name:		superkaramba-theme-%{theme}
Version:	1
Release:	0.2
License:	GPL 
Group:		Themes
Source0:	5882-xmmsbar-0.3.tar.gz
# Source0-md5:	47d0c28ff83c6d394814ea070233b208
URL:		http://www.kde-look.org/content/show.php?content=5882
Requires:	superkaramba
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xmmsbar theme for superkaramba.

%description -l pl
Motyw xmmsbar do superkaramba.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/xmmsbar/pics  \
    	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/xmmsbar/pics/.xvpics

install xmmsbar/*.theme $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/xmmsbar/
cp -a xmmsbar/*.py $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/xmmsbar/
%py_comp $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/xmmsbar/
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/xmmsbar/
rm -f $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/xmmsbar/*.py
install xmmsbar/pics/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/xmmsbar/pics/
install xmmsbar/pics/*.xcf $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/xmmsbar/pics/
install xmmsbar/pics/.xvpics/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/xmmsbar/pics/.xvpics/
install xmmsbar/pics/.xvpics/*.xcf $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/xmmsbar/pics/.xvpics/

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%dir %{_datadir}/themes/superkaramba/xmmsbar
%dir %{_datadir}/themes/superkaramba/xmmsbar/pics
%dir %{_datadir}/themes/superkaramba/xmmsbar/pics/.xvpics
%{_datadir}/themes/superkaramba/xmmsbar/*.theme
%{_datadir}/themes/superkaramba/xmmsbar/*.pyo
%{_datadir}/themes/superkaramba/xmmsbar/*.pyc
%{_datadir}/themes/superkaramba/xmmsbar/pics/*.png
%{_datadir}/themes/superkaramba/xmmsbar/pics/*.xcf
%{_datadir}/themes/superkaramba/xmmsbar/pics/.xvpics/*.png
%{_datadir}/themes/superkaramba/xmmsbar/pics/.xvpics/*.xcf
