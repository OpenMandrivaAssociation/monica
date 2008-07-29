Name:           monica
Version:        3.7
Release:        %mkrel 3
Summary:        Monitor Calibration Tool
License:        BSD
Group:          System/Kernel and hardware
URL:            http://www.pcbypaul.com/software/monica.html
Source0:        http://www.pcbypaul.com/software/dl/monica-%{version}.tar.bz2
Requires:       xgamma
BuildRequires:  fontconfig
BuildRequires:  fltk-devel
BuildRequires:  libxext-devel
BuildRequires:  libxft-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Monica is a monitor calibration tool. It works as frontend to xgamma to
alter the gamma correction for XFree86 or Xorg. The black point, gray,
and color blocks help to find usable settings for a target of 2.2 gamma,
the Web, and sRGB standard.

%prep
%setup -q

%build
%{make} CXX="g++ %{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__cp} -a monica %{buildroot}%{_bindir}/monica

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
#%%doc AUTHORS ChangeLog INSTALL LICENCE NEWS README
%doc authors ChangeLog install licence news readme
%attr(0755,root,root) %{_bindir}/monica

