Name:           monica
Version:        3.7
Release:        8
Summary:        Monitor Calibration Tool
License:        BSD
Group:          System/Kernel and hardware
URL:            http://www.pcbypaul.com/software/monica.shtml
Source0:        http://www.pcbypaul.com/software/dl/monica-%{version}.tar.bz2
Patch0:		monica-3.7-use-ldflags.patch
Patch1:		monica-3.7-mdv-fix-gcc43.patch
patch2:		monica-3.7-mdv-fix-str-fmt.patch
Requires:       xgamma
BuildRequires:  fltk-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Monica is a monitor calibration tool. It works as frontend to xgamma to
alter the gamma correction for XFree86 or Xorg. The black point, gray,
and color blocks help to find usable settings for a target of 2.2 gamma,
the Web, and sRGB standard.

%prep
%setup -q
%patch0 -p0 -b .orig
%patch1 -p1 -b .gcc43
%patch2 -p1 -b .strfmt

%build
%{make} CFLAGS="%{optflags}" LDFLAGS="%{?ldflags}"

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__cp} -a monica %{buildroot}%{_bindir}/monica

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc authors ChangeLog install licence news readme
%attr(0755,root,root) %{_bindir}/monica



%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 3.7-7mdv2011.0
+ Revision: 612922
- the mass rebuild of 2010.1 packages

* Thu Jan 21 2010 Jérôme Brenier <incubusss@mandriva.org> 3.7-6mdv2010.1
+ Revision: 494773
- fix build with gcc 4.3
- fix str fmt
- rebuild for new fltk

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Dec 14 2008 Funda Wang <fwang@mandriva.org> 3.7-4mdv2009.1
+ Revision: 314154
- use flags when compiling

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 3.7-3mdv2009.0
+ Revision: 252687
- rebuild

* Sun Jul 27 2008 David Walluck <walluck@mandriva.org> 3.7-1mdv2009.0
+ Revision: 250496
- 3.7

* Mon Dec 31 2007 David Walluck <walluck@mandriva.org> 3.6-1mdv2008.1
+ Revision: 139701
- import monica


