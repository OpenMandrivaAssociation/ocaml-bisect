Name:           ocaml-bisect
Version:        1.2
Release:        2
Summary:        OCaml code coverage tool
License:        GPLv3
Group:          Development/Other
URL:            https://bisect.x9c.fr/
Source0:        http://bisect.x9c.fr/distrib/bisect-%{version}.tar.gz
Source1:        http://bisect.x9c.fr/distrib/bisect.pdf
BuildRequires:  ocaml
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
%setup -q -n bisect-%{version}

%build
sh configure
make all doc

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export PATH_OCAML_BIN=%{_bindir}
mkdir -p $OCAMLFIND_DESTDIR/bisect
make install PATH_OCAML_BIN=%{_bindir}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/ocaml/bisect

install -m 0755 _build/src/report/report.native  %{buildroot}%{_bindir}/bisect-report
strip %{buildroot}%{_bindir}/bisect-report


%files
%defattr(-,root,root)
%doc COPYING
%dir %{_libdir}/ocaml/bisect
%{_bindir}/bisect-report
%{_libdir}/ocaml/bisect/*.cma
%{_libdir}/ocaml/bisect/*.cmi
%{_libdir}/ocaml/bisect/META
%{_libdir}/ocaml/bisect/*.cmo


%files devel
%defattr(-,root,root)
%doc CHANGES COPYING README VERSION doc/bisect.pdf ocamldoc
%{_libdir}/ocaml/bisect/*.a
%{_libdir}/ocaml/bisect/*.cmxa
%{_libdir}/ocaml/bisect/*.cmx



%changelog
* Sun Aug 09 2009 Florent Monnier <blue_prawn@mandriva.org> 1.0-3.beta.1mdv2010.0
+ Revision: 413656
- try to fix release field
- new increment
- incremented mkrel number
- corrected release field

* Sun Aug 09 2009 Florent Monnier <blue_prawn@mandriva.org> 1.0-1mdv2010.0
+ Revision: 412952
- spec file made from the fedora's one by Richard Jones

