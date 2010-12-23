Summary:	Ubuntu Font Family, sans-serif typeface hinted for clarity
Name:		ubuntu-font-family
Version:	0.69
Release:	1

Url:		http://font.ubuntu.com
License:	Ubuntu Font Licence 1.0
Group:		User Interface/X
Source0:	http://font.ubuntu.com/download/ubuntu-font-family-0.69+ufl.zip
BuildRoot:	%{_tmppath}/%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch

Requires(post):	fontconfig


%description
The Ubuntu Font Family are a set of matching new libre/open fonts in
development during 2010--2011. The development is being funded by
Canonical Ltd on behalf the wider Free Software community and the
Ubuntu project. The technical font design work and implementation is
being undertaken by Dalton Maag.

Both the final font Truetype/OpenType files and the design files used
to produce the font family are distributed under an open license and
you are expressly encouraged to experiment, modify, share and improve. 


%prep
%setup -q -n %{name}-%{version}+ufl


%build


%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/fonts/%{name}
install -m 644 *.ttf  $RPM_BUILD_ROOT%{_datadir}/fonts/%{name}

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/fontpath.d
cd $RPM_BUILD_ROOT%{_sysconfdir}/X11/fontpath.d
ln -s /usr/share/fonts/%{name}
cd -


%post 
if [ -x /usr/bin/fc-cache ]; then
    /usr/bin/fc-cache /usr/share/fonts/dejavu || :
fi


%postun
if [ $1 -eq 0 -a -x /usr/bin/fc-cache ] ; then
    /usr/bin/fc-cache /usr/share/fonts/dejavu || :
fi


%clean
rm -rf $RPM_BUILD_ROOT


%files 
%defattr(-,root,root,0755)  
%doc README.txt FONTLOG.txt LICENCE-FAQ.txt LICENCE.txt RELEASENOTES.txt TRADEMARKS.txt copyright.txt
%{_sysconfdir}/X11/fontpath.d/*
%{_datadir}/fonts/%{name}/*.ttf


%changelog
* Tue Oct 12 2010 Arkady L. Shane <ashejn@yandex-team.ru> 0.69-1
- initial build for Fedora
