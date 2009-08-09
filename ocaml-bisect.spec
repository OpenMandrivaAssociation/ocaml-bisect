%define mainversion 1.0
%define subversion beta

Name:           ocaml-bisect
Version:        %{mainversion}
Release:        %mkrel 1
Summary:        OCaml code coverage tool
License:        GPLv3
Group:          Development/Other
URL:            http://bisect.x9c.fr/
Source0:        http://bisect.x9c.fr/distrib/bisect-%{version}-%{subversion}.tar.gz
Source1:        http://bisect.x9c.fr/distrib/bisect.pdf
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml-findlib
BuildRequires:  camlp4

%description
Bisect is a code coverage tool for the Objective Caml language. It is
a camlp4-based tool that allows to instrument your application before
running tests. After application execution, it is possible to generate
a report in HTML format that is the replica of the application source
code annotated with code coverage information.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n bisect-%{version}-%{subversion}

%build
make all

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/ocaml/bisect

install -m 0755 bin/bisect-report.opt  %{buildroot}%{_bindir}/bisect-report
strip %{buildroot}%{_bindir}/bisect-report

install -m 0644 bin/*.{a,cmi,cma,cmx,cmxa}  %{buildroot}%{_libdir}/ocaml/bisect


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%dir %{_libdir}/ocaml/bisect
%{_bindir}/bisect-report
%{_libdir}/ocaml/bisect/*.cma
%{_libdir}/ocaml/bisect/*.cmi

%files devel
%defattr(-,root,root)
%doc CHANGES COPYING README VERSION doc/bisect.pdf ocamldoc
%{_libdir}/ocaml/bisect/*.a
%{_libdir}/ocaml/bisect/*.cmxa
%{_libdir}/ocaml/bisect/*.cmx

