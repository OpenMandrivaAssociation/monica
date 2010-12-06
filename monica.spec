Name:           monica
Version:        3.7
Release:        %mkrel 7
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

