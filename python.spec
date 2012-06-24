Summary:     Very high level scripting language with X interface
Summary(de): Very High-Level-Script-Sprache mit X-Oberfl�che
Summary(fr): Langage de script de t�s haut niveau avec interface X.
Summary(pl): Bardzo zaawansowany j�zyk do pisania skrypt�w
Summary(tr): X aray�zl�, y�ksek d�zeyli, kabuk yorumlay�c� dili
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
Python ist eine interpretierte, objektorientierte Scriptsprache. Sie unterst�tzt
dynamisches Laden von Objekten, Klassen, Modulen und Ausnahmen.
Das Hinzuf�gen von Schnittstellen zu neuen System-Libraries in C-Code ist,
einfach, wodurch sich Python m�helos in benutzerdefinierten Umgebungen
einsetzen l��t.
Dieses Python-Paket enth�lt die meisten standardm��igen Python-Module
sowie Module f�r Schnittstellen zum Tix widget set f�r Tk und RPM.

%description -l fr
Python est un langage de script interpr�t� et orient� objet. Il g�re le
chargement dynamique des objets, les classes, les modules et les exceptions.
L'ajout d'interfaces aux nouvelles biblioth�ques syst�mes avec du code C est
simple, ce qui rend Python facile � utiliser dans des configs personnalis�es.

Ce paquetage Python contient la plupart des modules Python standards, ainsi
que ceux permettant l'interfa�age avec les widgets Tix pour Tk et RPM.

%description -l pl
Python to zorientowany obiektowo j�zyk do pisania sktypt�w. Zawiera
wsparcie do dynamicznego �adowania obiekt�w, klas, mod��w i wyj�tk�w.
Dodawanie interfejs�w do nowo powstaj�cych bibliotek systemowych poprzez
napisanie w jezyku C modu��w do Pythona jest bezproblemowe. Sprawia to, �e
Python jest �atwy do u�ycia w r�nych zastosowaniach. 

%description -l tr
Python, nesneye y�nelik bir kabuk yorumlay�c�d�r. Nesnelerin, s�n�flar�n,
mod�llerin ve ayk�r� durumlar�n dinamik y�klenmelerine destek verir. C
koduyla birlikte kullan�m� son derece kolayd�r. Bu paket, standart Python
birimlerinin �o�unun yan�s�ra Tk ve RPM i�in aray�z birimlerini de i�erir.

%package devel
Summary:     Libraries and header files for building python code
Summary(de): Libraries und Header-Dateien zum Erstellen von Python-Code
Summary(fr): Biblioth�ques et en-t�tes pour construire du code python
Summary(pl): Pliki nag��wkowe i biblioteki python
Summary(tr): Python ile geli�tirme yapmak i�in gerekli dosyalar
Group:       Development/Languages
Requires:    %{name} = %{version}

%description devel
The Python interpreter is relatively easy to extend with dynamically loaded
extensions and to embed in other programs. This packages contains the
header files and libraries which are needed to do both of these tasks.

%description -l de devel
Der Python-Interpretierer ist relativ einfach anhand von dynamisch 
ladbaren Erweiterungen auszubauen und l��t sich in andere 
Programme integrieren. Dieses Paket enth�lt die Header-Dateien und 
Libraries, die f�r beide Aufgaben erforderlich sind. 

%description -l fr devel
L'interpr�teur Python est relativement facile � �tendre avec des extensions
charg�es dynamiquement et � ins�rer dans d'autres programmes. Ce paquetage
contient les en-t�tes et les biblioth�ques n�cessaires � ces deux t�ches.

%description -l pl devel
Wszystko czego potrzeba aby napisa� w C/C++ modu� rozszerzaj�cy mo�liwo�ci
Pythona.

%description -l tr devel
Bu paket, Python ile geli�tirme yap�labilmesi i�in gerekli ba�l�k dosyalar�n�
ve kitapl�klar� i�erir.

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
Dieses Paket enth�lt Dokumentationen zu Python (Sprache und Interpreter)
in Form von einfachen ASCII-Dateien und LaTeX-Quellen.

%description -l fr docs
Ce paquetage contient la documentation sur le langage python et sur son
interpr�teur sous forme de fichiers ASCII et LaTeX.

%description -l pl docs
Oficjalna dokumentacja do Pythona. Zawiera programy przyk�adowe, narz�dzia
i dokumentacje. Strony do manuala znajduj� sie w g��wnym pakiecie.
Ten pakiet nie zawiera �r�de� dokumentacji napisanych w LaTeX'u,
tylko Gotowe do wykorzystania pliki postscript'owe i html. 

%description -l tr docs
Bu paket, Python dili ile ilgili belgeleri ve d�z ASCII dosyalar� ve LaTeX
kaynaklar�n�n bir kar���m� olan yorumlay�c�y� i�erir.

%package -n tkinter
Summary:     GUI interface for Python
Summary(de): Grafischer Oberfl�che f�r Python
Summary(fr): Interface graphique pour python.
Summary(pl): GUI dla Pythona
Summary(tr): Python i�in grafik kullan�c� aray�z�
Group:       Development/Languages
Requires:    %{name} = %{version}
Requires:    tcl >= 8.0.3 
Requires:    tk  >= 8.0.3

%description -n tkinter
A graphical interface for Python, based on Tcl/Tk, and used by many of
the configuration tools.

%description -l pl -n tkinter 
Interfejs graficzny dla Puyhone, bazuj�cy na Tcl/Tk. Program ten jest u�ywany
przez wiele program�w konfiguracyjnych.

%description -l de -n tkinter
Eine grafische Schnittstelle f�r Python, basierend auf Tcl/Tk, und von 
vielen Konfigurations-Tools genutzt. 

%description -l fr -n tkinter
Interface graphique pour Python, bas�e sur Tcl/Tk et utilis�e par beaucoup
des outils de configuration.

%description -l tr -n tkinter
Python i�in Tcl/Tk'ye dayal� ve pek �ok ayarlama arac� taraf�ndan kullan�lan
grafik bir aray�zd�r.

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
* Wed Nov 25 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5.1-6]
- added URL.

* Sun Nov 15 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
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
