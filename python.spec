Summary:     Very high level scripting language with X interface
Summary(de): Very High-Level-Script-Sprache mit X-Oberfläche
Summary(fr): Langage de script de tés haut niveau avec interface X.
Summary(pl): Bardzo zaawansowany jêzyk do pisania skryptów
Summary(tr): X arayüzlü, yüksek düzeyli, kabuk yorumlayýcý dili
Name:        python
Version:     1.5.1
Release:     6
Copyright:   distributable
Group:       Development/Languages
Source:      ftp://ftp.python.org/pub/python/src/pyth151.tgz
Source1:     Python-Doc.tar.gz
Patch:       %{name}-%{version}-config.patch
Patch1:      %{name}-1.4-gccbug.patch
Patch2:      %{name}-1.5-localbin.patch
Patch3:      Python-1.5.1-nosed.patch
URL:         http://www.python.org/
Buildroot:   /tmp/%{name}-%{version}-root

%description
Python in an interpreted, object orientated scripting language. If contains
support for dynamic loading of objects, classes, modules, and exceptions.
Adding interfaces to new system libraries through C code is straightforward,
making Python easy to use in custom settings. 

This Python package includes most of the standard Python modules, along with
modules for interfacing to the Tix widget set for Tk and RPM.

%description -l de
Python ist eine interpretierte, objektorientierte Scriptsprache. Sie unterstützt
dynamisches Laden von Objekten, Klassen, Modulen und Ausnahmen.
Das Hinzufügen von Schnittstellen zu neuen System-Libraries in C-Code ist,
einfach, wodurch sich Python mühelos in benutzerdefinierten Umgebungen
einsetzen läßt.
Dieses Python-Paket enthält die meisten standardmäßigen Python-Module
sowie Module für Schnittstellen zum Tix widget set für Tk und RPM.

%description -l fr
Python est un langage de script interprété et orienté objet. Il gère le
chargement dynamique des objets, les classes, les modules et les exceptions.
L'ajout d'interfaces aux nouvelles bibliothèques systèmes avec du code C est
simple, ce qui rend Python facile à utiliser dans des configs personnalisées.

Ce paquetage Python contient la plupart des modules Python standards, ainsi
que ceux permettant l'interfaçage avec les widgets Tix pour Tk et RPM.

%description -l pl
Python to zorientowany obiektowo jêzyk do pisania sktyptów. Zawiera
wsparcie do dynamicznego ³adowania obiektów, klas, modó³ów i wyj±tków.
Dodawanie interfejsów do nowo powstaj±cych bibliotek systemowych poprzez
napisanie w jezyku C modu³ów do Pythona jest bezproblemowe. Sprawia to, ¿e
Python jest ³atwy do u¿ycia w ró¿nych zastosowaniach. 

%description -l tr
Python, nesneye yönelik bir kabuk yorumlayýcýdýr. Nesnelerin, sýnýflarýn,
modüllerin ve aykýrý durumlarýn dinamik yüklenmelerine destek verir. C
koduyla birlikte kullanýmý son derece kolaydýr. Bu paket, standart Python
birimlerinin çoðunun yanýsýra Tk ve RPM için arayüz birimlerini de içerir.

%package devel
Summary:     Libraries and header files for building python code
Summary(de): Libraries und Header-Dateien zum Erstellen von Python-Code
Summary(fr): Bibliothèques et en-têtes pour construire du code python
Summary(pl): Pliki nag³ówkowe i biblioteki python
Summary(tr): Python ile geliþtirme yapmak için gerekli dosyalar
Group:       Development/Languages
Requires:    %{name} = %{version}

%description devel
The Python interpreter is relatively easy to extend with dynamically loaded
extensions and to embed in other programs. This packages contains the
header files and libraries which are needed to do both of these tasks.

%description -l de devel
Der Python-Interpretierer ist relativ einfach anhand von dynamisch 
ladbaren Erweiterungen auszubauen und läßt sich in andere 
Programme integrieren. Dieses Paket enthält die Header-Dateien und 
Libraries, die für beide Aufgaben erforderlich sind. 

%description -l fr devel
L'interpréteur Python est relativement facile à étendre avec des extensions
chargées dynamiquement et à insérer dans d'autres programmes. Ce paquetage
contient les en-têtes et les bibliothèques nécessaires à ces deux tâches.

%description -l pl devel
Wszystko czego potrzeba aby napisaæ w C/C++ modu³ rozszerzaj±cy mo¿liwo¶ci
Pythona.

%description -l tr devel
Bu paket, Python ile geliþtirme yapýlabilmesi için gerekli baþlýk dosyalarýný
ve kitaplýklarý içerir.

%package docs
Summary:     Documentation on Python
Summary(de): Dokumentation zu Python 
Summary(fr): Documentation sur Python
Summary(pl): Dokumentacja do Python'a 
Summary(tr): Python belgeleri
Group:       Development/Languages
Requires:    %{name} = %{version}

%description docs
This package contains documentation on the Python language and interpretor
as a mix of plain ASCII files and LaTeX sources.

%description -l de docs
Dieses Paket enthält Dokumentationen zu Python (Sprache und Interpreter)
in Form von einfachen ASCII-Dateien und LaTeX-Quellen.

%description -l fr docs
Ce paquetage contient la documentation sur le langage python et sur son
interpréteur sous forme de fichiers ASCII et LaTeX.

%description -l pl docs
Oficjalna dokumentacja do Pythona. Zawiera programy przyk³adowe, narzêdzia
i dokumentacje. Strony do manuala znajduj± sie w g³ównym pakiecie.
Ten pakiet nie zawiera ¼róde³ dokumentacji napisanych w LaTeX'u,
tylko Gotowe do wykorzystania pliki postscript'owe i html. 

%description -l tr docs
Bu paket, Python dili ile ilgili belgeleri ve düz ASCII dosyalarý ve LaTeX
kaynaklarýnýn bir karýþýmý olan yorumlayýcýyý içerir.

%package -n tkinter
Summary:     GUI interface for Python
Summary(de): Grafischer Oberfläche für Python
Summary(fr): Interface graphique pour python.
Summary(pl): GUI dla Pythona
Summary(tr): Python için grafik kullanýcý arayüzü
Group:       Development/Languages
Requires:    %{name} = %{version}
Requires:    tcl >= 8.0.3 
Requires:    tk  >= 8.0.3

%description -n tkinter
A graphical interface for Python, based on Tcl/Tk, and used by many of
the configuration tools.

%description -l pl -n tkinter 
Interfejs graficzny dla Puyhone, bazuj±cy na Tcl/Tk. Program ten jest u¿ywany
przez wiele programów konfiguracyjnych.

%description -l de -n tkinter
Eine grafische Schnittstelle für Python, basierend auf Tcl/Tk, und von 
vielen Konfigurations-Tools genutzt. 

%description -l fr -n tkinter
Interface graphique pour Python, basée sur Tcl/Tk et utilisée par beaucoup
des outils de configuration.

%description -l tr -n tkinter
Python için Tcl/Tk'ye dayalý ve pek çok ayarlama aracý tarafýndan kullanýlan
grafik bir arayüzdür.

%prep
%setup -q -n Python-1.5.1 -a1
%patch -p1 
%patch2 -p1
%patch3 -p1 

find . -name "*.nosed" -exec rm -f {} \;

echo ': ${LDSHARED='gcc -shared'}' > config.cache
echo ': ${LINKFORSHARED='-rdynamic'}' >> config.cache
echo ': ${CCSHARED='-fPIC'}' >> config.cache

cp Lib/lib-old/rand.py Lib

%build
LDFLAGS=-s MACHDEP=linux-$RPM_ARCH \
./configure %{_target} \
	--prefix=/usr --with-threads

make OPT="$RPM_OPT_FLAGS -D_REENTRANT"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,lib}

make install prefix=$RPM_BUILD_ROOT/usr

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc README

%attr(755,root,root) %{_bindir}/*

%dir %{_libdir}/python1.5
%attr(-,root,root) %{_libdir}/python1.5/*.py
%attr(-,root,root) %{_libdir}/python1.5/*.pyc
%attr(-,root,root) %{_libdir}/python1.5/*.pyo

%dir %{_libdir}/python1.5/lib-dynload
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/*.so

%dir %{_libdir}/python1.5/lib-stdwin
%attr(755,root,root) %{_libdir}/python1.5/lib-stdwin/*.py
%{_libdir}/python1.5/lib-stdwin/*.pyc
%{_libdir}/python1.5/lib-stdwin/*.pyo

%dir %{_libdir}/python1.5/plat-linux-%{buildarch}
%attr(755,root,root) %{_libdir}/python1.5/plat-linux-%{buildarch}/regen
%{_libdir}/python1.5/plat-linux-%{buildarch}/*.py
%{_libdir}/python1.5/plat-linux-%{buildarch}/*.pyc
%{_libdir}/python1.5/plat-linux-%{buildarch}/*.pyo

%files devel
%defattr(644,root,root,755)

%dir /usr/include/python1.5
/usr/include/python1.5/*.h

%dir %{_libdir}/python1.5/config
%attr(-,root,root) %{_libdir}/python1.5/config/*

%dir %{_libdir}/python1.5/test
%attr(-,root,root,755) %{_libdir}/python1.5/test/*

%files docs
%defattr(645,root,root,755)
%doc Misc/COPYRIGHT Misc/NEWS Misc/HYPE Misc/README Misc/cheatsheet 
%doc Misc/HISTORY Doc Misc/BLURB* 

%files -n tkinter
%defattr(644,root,root,755)

%dir %{_libdir}/python1.5/lib-tk
%attr(-,root,root) %{_libdir}/python1.5/lib-tk/*

%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/_tkinter.so

%changelog
* Wed Nov 25 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5.1-6]
- added URL.

* Sun Nov 15 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.5.1-1]
- build for PLD Linux,
- added pl translation,
- major changes.

* Thu Sep  3 1998 Jeff Johnson <jbj@redhat.com>
- recompile for RH 5.2.

* Wed May 06 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- python-docs used to require %{_bindir}/sed. Changed to /bin/sed instead

* Wed Apr 29 1998 Cristian Gafton <gafton@redhat.com>
- fixed the spec file for version 1.5.1
- buildroot (!)

* Mon Apr 20 1998 Michael K. Johnson <johnsonm@redhat.com>
- updated to python 1.5.1
- created our own Python-Doc tar file from 1.5 to substitute for the
  not-yet-released Doc package.
- build _tkinter properly
- use readline again
- build crypt module again
- install rand replacement module
- added a few modules

* Thu Apr 09 1998 Erik Troan <ewt@redhat.com>
- updated to python 1.5
- made %{_libdir}/python1.5 file list automatically generated

* Tue Nov 04 1997 Michael K. Johnson <johnsonm@redhat.com>
- Fixed dependencies for python and tkinter

* Mon Nov 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- pulled out tk-related stuff into tkinter package

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- bunches of scripts used /usr/local/bin/python instead of %{_bindir}/python

* Tue Sep 30 1997 Erik Troan <ewt@redhat.com>
- updated for tcl/tk 8.0

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
