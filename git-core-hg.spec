Summary:	Git tools for working with mercurial repositories
Name:		git-core-hg
Version:	0.6
Release:	1
Epoch:		1
License:	GPL v2
Group:		Development/Tools
Source0:	https://github.com/felipec/git-remote-hg/archive/refs/tags/v%{version}.tar.gz
# Source0-md5:	8a1acaba6d5f2acd453870b136695eba
URL:		https://github.com/felipec/git-remote-hg
BuildRequires:	rpm-pythonprov
Requires:	git-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Git tools for working with mercurial repositories.

%define         gitcoredir      %{_libexecdir}/git-core

%prep
%setup -q -n git-remote-hg-%{version}

%{__sed} -i -e '1s,/usr/bin/env python$,%{__python3},' git-remote-hg

%build
%{__make} \
	V=1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{gitcoredir},%{_mandir}/man1}

cp -p git-remote-hg $RPM_BUILD_ROOT%{gitcoredir}
cp -p doc/git-remote-hg.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.asciidoc
%attr(755,root,root) %{gitcoredir}/git-remote-hg
%{_mandir}/man1/git-remote-hg.1*
