Summary:	Very high level scripting language with X interface
Summary(de):	Very High-Level-Script-Sprache mit X-Oberfläche
Summary(fr):	Langage de script de tés haut niveau avec interface X.
Summary(pl):	Python - obiektowy jezyk do tworzenia skryptów (g³ówny pakiet)
Summary(tr):	X arayüzlü, yüksek düzeyli, kabuk yorumlayýcý dili
Name:		python
Version:	1.5.2
Release:	6
Copyright:	distributable
Group:		Development/Languages
Source0:	ftp://ftp.python.org/pub/python/src/pyth152.tgz
Source1:	Python-Doc.tar.gz
Patch0:		%{name}-%{version}-config.patch
Patch1:		%{name}-1.4-gccbug.patch
Patch2:		%{name}-1.5-localbin.patch
Patch3:		Python-1.5.1-nosed.patch
URL:		http://www.python.org/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Python is an interpreted, interactive, object-oriented programming language. 
It incorporates modules, exceptions, dynamic typing, very high level dynamic
data types, and classes. Python combines remarkable power with very clear
syntax. It has interfaces to many system calls and libraries, as well as to
various window systems, and is extensible in C or C++. It is also usable as
an extension language for applications that need a programmable interface. 
Finally, Python is portable: it runs on many brands of UNIX, on the Mac, and
on PCs under MS-DOS, Windows, Windows NT, and OS/2.

To find out more, the best thing to do is to start reading the tutorial from
the documentation set at <http://www.python.org/doc/>."

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
Python jest interpretowanym, interaktywnym i "zorientowanym obiektowo"
jêzykiem programowania. Jest modularny, obs³uguje wyj±tki, dynamiczne typy,
zaawansowane dynamiczne struktury danych i klasy. Python ³±czy w sobie du¿e
mo¿liwo¶ci i przejrzyst± sk³adnie. Posiada interfejsy do wielu wywo³añ
systemowych i bibliotek, w tym rówie¿ do ró¿nych bibliotek okienkowych.
Mo¿liwo¶ci jego mo¿na jeszcze rozdze¿aæ poprzez odpowiednie modu³y pisane w
C lub C++. Python mo¿e byæ równie¿ u¿yty jako element aplikacji, którym
potrzebny jest interpreter do skryptów. I wreszcie, Python jest
wieloplatformowy, dzia³a na wielu odmianach UNIX'a, Mac'u oraz PC pod
DOS'em, Windows, WindowsNT oraz OS/2.

Aby lepiej poznaæ Pythona, najlepsz± rzecz± jest zapoznanie siê z
wprowadzeniem (tutorial) wchodz±cym w sk³ad dokumentacji Pythona znajduj±cej
siê na <http://www.python.org/doc/>.

%description -l tr
Python, nesneye yönelik bir kabuk yorumlayýcýdýr. Nesnelerin, sýnýflarýn,
modüllerin ve aykýrý durumlarýn dinamik yüklenmelerine destek verir. C
koduyla birlikte kullanýmý son derece kolaydýr. Bu paket, standart Python
birimlerinin çoðunun yanýsýra Tk ve RPM için arayüz birimlerini de içerir.

%package devel
Summary:	Libraries and header files for building python code
Summary(de):	Libraries und Header-Dateien zum Erstellen von Python-Code
Summary(fr):	Bibliothèques et en-têtes pour construire du code python
Summary(pl):	Pliki nag³ówkowe i biblioteki python
Summary(tr):	Python ile geliþtirme yapmak için gerekli dosyalar
Group:		Development/Languages
Requires:	%{name} = %{version}

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
Summary:	Documentation on Python
Summary(de):	Dokumentation zu Python 
Summary(fr):	Documentation sur Python
Summary(pl):	Dokumentacja do Python'a 
Summary(tr):	Python belgeleri
Group:		Development/Languages
Requires:	%{name} = %{version}

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
Summary:	Lowlevel Python -> Tk Interface
Summary(de):	Grafischer Oberfläche für Python
Summary(fr):	Interface graphique pour python.
Summary(pl):	modu³y niskiego poziomu dla pakietu Python-tkinter
Summary(tr):	Python için grafik kullanýcý arayüzü
Group:		Development/Languages/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	%{name} = %{version}
Requires:	tcl >= 8.0.3 
Requires:	tk  >= 8.0.3
Requires:	blt >= 2.4c
Requires:	tix >= 4.1.0.6

%description -n tkinter
This is the lowlevel C module that interfaces Tk and which is the basis for
the Tkinter, Python's OO interface to Tk, which is included in the package
python-tkinter.

The only reason this file is removed from python-tkinter, is to make it more
easy to replay _tkinter with a PIL (Python Imaging Libary) aware version of
it. Look at my PIL distribution.

%description -l de -n tkinter
Eine grafische Schnittstelle für Python, basierend auf Tcl/Tk, und von 
vielen Konfigurations-Tools genutzt. 

%description -l fr -n tkinter
Interface graphique pour Python, basée sur Tcl/Tk et utilisée par beaucoup
des outils de configuration.

%description -l pl -n tkinter 
Ten pakiet zawiera modu³y w C, które po¶rednicz± w wywo³aniach pomiêdzy
samym Tk a modu³em Tkinter bêd±cym g³ownym interfejsem Tk dla Pythona.
Tkinter jets dostêpny w pakiecie python-tkinter.rpm

Jedynym powodem wdzielenia tego pakietu jest u³atwienie wymiany go na PIL
(Python Imaging Library).

%description -l tr -n tkinter
Python için Tcl/Tk'ye dayalý ve pek çok ayarlama aracý tarafýndan kullanýlan
grafik bir arayüzdür.

%package demos
Summary:	Demoscripts and tools for/in Python
Summary:	Dema i skrypty narzêdziowe do/z Pythona
Group:		Development/Languages/Python
Group(pl):	Programowanie/Jêzyki/Python
Icon:		linux-python-doc-icon.gif
Requires:	%{name} = %{version}

%description demos
The package contains the demos and tools distributed along with the Python
source distribution.

The demos cover nearly all aspects of Python and all fields Python can be
used in.

The tools are

	audiopy - program struj±cy urz±dzeniem dzwiêkowym w Solarisie.  BGEN
	-- Automatic Generation of Extension Modules.  FAQ Wizard -- skrypt
	CGI do zarz±dzania baz± pytañ FAQ. THE FREEZE SCRIPT -- Freeze
	umo¿liwia "wyeksportowanie" skryptów w Pythonie na maszyny na
	których nie jest on zainstalowany.  programs to people who don't
	have Python.

	IDLE -- a Tkinter-based IDE for Python
	modulator -- generuje kod w C do pisania nowych modu³ów dla Pythona.
	Pynche -- The PYthonically Natural Color and Hue Editor
	Webchecker -- Prosty program przeszukij±cy drzewo WWW w poszukiwaniu
		      na przyk³ad nie istniej±cych linków.
	world -- wy¶wietla nazwy pañstw i odpowiadaj±ce im domeny w DNS

%description -l pl demos
Ten pakiet zawiera przyk³adowe programy i narzêdzia znajduj±ce siê w 
¼ród³owej dystrybucji Pythona.

Dema obrazuj± prawie wszystkie cechy Pythona i zastosowania w których mo¿e
on byæ u¿yty.

Zawatre w pakiecie narzêdzia to:

	audiopy - program do sterowania urz±dzeniem dzwiêkowym w Solarisie.
	BGEN -- Automatyczny generator modu³ów rozszerzaj±cych.
	FAQ Wizard -- skrypt CGI do zarz±czania baz± pytañ (FAQ).
	THE FREEZE SCRIPT -- Freeze make it possible to ship arbitrary Python
			 programs to people who don't have Python.
	IDLE -- napisane z Tkinter ¶rodowisko programistyczne (IDE) do Pythona
	modulator -- a generator of boilerplate code for modules to be written in C.
	Pynche -- The PYthonically Natural Color and Hue Editor
	Webchecker -- This is a simple web tree checker, useful to find bad links in
								a web tree.
	world -- Print mappings between country names and DNS country codes

%package gdbm
Summary:	Python interface to the GDBM library
Summary(pl):	Interfejs do biblioteki GDBM dla Pythona
Group:		Development/Languages/Python
Group(pl):	Programowanie/Jêzyki/Python
Icon:		linux-python-db-icon.gif
Requires:	%{name} =%{version}

%description gdbm
An easy to use interface to GDBM databases. GDBM is the GNU implementation
of the standard unix dbm databases.

%description -l pl gdbm
Interfejs do baz danych GDBM dla Pythona. GDBM to implementacja
standarwowych unixowych baz danych DBM zrealizowana przez GNU.

%package curses
Summary:	Python interface to the (n)curses library
Summary(pl):	Interfejs do biblioteki (n)curses dla Pythona
Group:		Development/Languages/Python
Icon:		linux-python-curses-icon.gif
Requires:	%{name} =%{version}

%description curses
An easy to use interface to (n)curses CUI library. CUI stands for console
user interface.

%description curses
Interfejs do biblioteki (n)curses. curses do biblioteka uno¿liwiaj±ce tworzenie
okienkowego interfejsu u¿ytkownika na terminalu tekstowym.

%package zlib
Summary:	Python interface to the zlib library
Summary(pl):	Interfejs do biblioteki zlib  dla Pythona
Group:		Development/Languages/Python
Group(pl):	Programowanie/Jêzyki/Python
Icon:		linux-python-zlib-icon.gif
Requires:	%{name} =%{version}

%description zlib
An interface to the zlib library. zlib offers the gzip algorithms for
applications programmers.

%description -l pl zlib
Interfejs do biblioteki zlib dla Pythona. Zlib udostêpnia algorytmy
kompresji u¿ywane przez gzip'a.

%prep
%setup -q -n Python-1.5.1 -a1
%patch0 -p1 
%patch2 -p1
%patch3 -p1 

find . -name "*.nosed" -exec rm -f {} \;

echo ': ${LDSHARED='gcc -shared'}' > config.cache
echo ': ${LINKFORSHARED='-rdynamic'}' >> config.cache
echo ': ${CCSHARED='-fPIC'}' >> config.cache

cp Lib/lib-old/rand.py Lib

%build
LDFLAGS=-s MACHDEP=linux-$RPM_ARCH \
./configure %{_target_platform} \
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

%dir %{_includedir}/python1.5
%{_includedir}/python1.5/*.h

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
* Sun Jun  6 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5.2-1]
- based on RH spec,
- spec rewrited by PLD team,
- pl translation by Wojtek ¦lusarczyk <wojtek@shadow.eu.org>.
