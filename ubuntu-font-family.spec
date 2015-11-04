Name:           ubuntu-font-family
Version:        0.83
Release:        1%{?dist}
Summary:        This is the Ubuntu Font Family

License:        Ubuntu Font License 1.0
URL:            http://font.ubuntu.com/
Source0:        http://font.ubuntu.com/download/%{name}-%{version}.zip

BuildArch:      noarch

%description
It is a unique, custom designed font that has a very distinctive look and feel.

%prep
%setup -q

mv LICENCE.txt LICENSE.txt
mv LICENCE-FAQ.txt LICENSE-FAQ.txt

# fix https://bugs.launchpad.net/ubuntu-font-family/+bug/744812 issue:
# wrong font rendering for qt applications
rm Ubuntu-M.ttf Ubuntu-MI.ttf

%build
# not build

%install
for font in `ls | grep ttf`; do
    %{__install} -D -m 0644 $font %{buildroot}%{_datadir}/fonts/%{name}/$font
done

%post
if [ -x /usr/bin/fc-cache ]; then
    /usr/bin/fc-cache /usr/share/fonts/dejavu || :
fi

%postun
if [ $1 -eq 0 -a -x /usr/bin/fc-cache ] ; then
    /usr/bin/fc-cache /usr/share/fonts/dejavu || :
fi

%files
%doc CONTRIBUTING.txt FONTLOG.txt README.txt TRADEMARKS.txt
%license copyright.txt LICENSE.txt LICENSE-FAQ.txt
%{_datadir}/fonts/%{name}

%changelog
* Wed Nov 04 2015 Maxim Orlov <murmansksity@gmail.com> - 0.83-1.R
- Update to 0.83

* Fri Nov 11 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 0.69-2.R
- Revert to 0.69

* Fri Sep 30 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 0.80-1.R
- Update to 0.80

* Tue Oct 12 2010 Arkady L. Shane <ashejn@yandex-team.ru> 0.69-1
- initial build for Fedora
