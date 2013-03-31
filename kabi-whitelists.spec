Name:		kabi-whitelists
Version:	20101015
Release:	1%{?dist}.1
Summary:	The Red Hat Enterprise Linux kernel ABI symbol whitelists

Group:		System Environment/Kernel
License:	GPLv2
URL:		http://www.redhat.com/
Source0:	kabi-whitelists-%{version}.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

%description
The kABI package contains information pertaining to the Red Hat Enterprise
Linux kernel ABI, including lists of kernel symbols that are needed by
external Linux kernel modules, and a yum plugin to aid enforcement.

%prep
%setup -q

%build
# nothing to build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/lib/modules/kabi
cp kabi_whitelist_{i686,ppc64,s390x,x86_64} $RPM_BUILD_ROOT/lib/modules/kabi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/lib/modules/kabi

%changelog
* Sat Oct 16 2010 Jon Masters <jcm@redhat.com> - 20101015-1
- Update the kABI whitelists for RHEL6.0 GA release
- Resolves: #643570

* Fri Aug 20 2010 Jon Masters <jcm@redhat.com> - 20100820-1
- Update the kABI whitelists for snapshot 13 release
- Resolves: #612735

* Tue Aug 17 2010 Jon Masters <jcm@redhat.com> - 20100817-1
- Update the kABI whitelists for snapshot 12 release
- Resolves: #612735

* Wed May 12 2010 Jon Masters <jcm@redhat.com> - 20100512-2
- Initial public build of kABI whitelists package
- Resolves: #591675
