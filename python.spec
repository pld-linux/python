Summary:	Very high level scripting language with X interface
Summary(de):	Very High-Level-Script-Sprache mit X-Oberfl�che
Summary(fr):	Langage de script de t�s haut niveau avec interface X.
Summary(pl):	Python - obiektowy jezyk do tworzenia skrypt�w (g��wny pakiet)
Summary(tr):	X aray�zl�, y�ksek d�zeyli, kabuk yorumlay�c� dili
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
Python jest interpretowanym, interaktywnym i "zorientowanym obiektowo"
j�zykiem programowania. Jest modularny, obs�uguje wyj�tki, dynamiczne typy,
zaawansowane dynamiczne struktury danych i klasy. Python ��czy w sobie du�e
mo�liwo�ci i przejrzyst� sk�adnie. Posiada interfejsy do wielu wywo�a�
systemowych i bibliotek, w tym r�wie� do r�nych bibliotek okienkowych.
Mo�liwo�ci jego mo�na jeszcze rozdze�a� poprzez odpowiednie modu�y pisane w
C lub C++. Python mo�e by� r�wnie� u�yty jako element aplikacji, kt�rym
potrzebny jest interpreter do skrypt�w. I wreszcie, Python jest
wieloplatformowy, dzia�a na wielu odmianach UNIX'a, Mac'u oraz PC pod
DOS'em, Windows, WindowsNT oraz OS/2.

Aby lepiej pozna� Pythona, najlepsz� rzecz� jest zapoznanie si� z
wprowadzeniem (tutorial) wchodz�cym w sk�ad dokumentacji Pythona znajduj�cej
si� na <http://www.python.org/doc/>.

%description -l tr
Python, nesneye y�nelik bir kabuk yorumlay�c�d�r. Nesnelerin, s�n�flar�n,
mod�llerin ve ayk�r� durumlar�n dinamik y�klenmelerine destek verir. C
koduyla birlikte kullan�m� son derece kolayd�r. Bu paket, standart Python
birimlerinin �o�unun yan�s�ra Tk ve RPM i�in aray�z birimlerini de i�erir.

%package devel
Summary:	Libraries and header files for building python code
Summary(de):	Libraries und Header-Dateien zum Erstellen von Python-Code
Summary(fr):	Biblioth�ques et en-t�tes pour construire du code python
Summary(pl):	Pliki nag��wkowe i biblioteki python
Summary(tr):	Python ile geli�tirme yapmak i�in gerekli dosyalar
Group:		Development/Languages
Requires:	%{name} = %{version}

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
Summary:	Lowlevel Python -> Tk Interface
Summary(de):	Grafischer Oberfl�che f�r Python
Summary(fr):	Interface graphique pour python.
Summary(pl):	modu�y niskiego poziomu dla pakietu Python-tkinter
Summary(tr):	Python i�in grafik kullan�c� aray�z�
Group:		Development/Languages/Python
Group(pl):	Programowanie/J�zyki/Python
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
Eine grafische Schnittstelle f�r Python, basierend auf Tcl/Tk, und von 
vielen Konfigurations-Tools genutzt. 

%description -l fr -n tkinter
Interface graphique pour Python, bas�e sur Tcl/Tk et utilis�e par beaucoup
des outils de configuration.

%description -l pl -n tkinter 
Ten pakiet zawiera modu�y w C, kt�re po�rednicz� w wywo�aniach pomi�dzy
samym Tk a modu�em Tkinter b�d�cym g�ownym interfejsem Tk dla Pythona.
Tkinter jets dost�pny w pakiecie python-tkinter.rpm

Jedynym powodem wdzielenia tego pakietu jest u�atwienie wymiany go na PIL
(Python Imaging Library).

%description -l tr -n tkinter
Python i�in Tcl/Tk'ye dayal� ve pek �ok ayarlama arac� taraf�ndan kullan�lan
grafik bir aray�zd�r.

%package demos
Summary:	Demoscripts and tools for/in Python
Summary:	Dema i skrypty narz�dziowe do/z Pythona
Group:		Development/Languages/Python
Group(pl):	Programowanie/J�zyki/Python
Icon:		linux-python-doc-icon.gif
Requires:	%{name} = %{version}

%description demos
The package contains the demos and tools distributed along with the Python
source distribution.

The demos cover nearly all aspects of Python and all fields Python can be
used in.

The tools are

	audiopy - program struj�cy urz�dzeniem dzwi�kowym w Solarisie.  BGEN
	-- Automatic Generation of Extension Modules.  FAQ Wizard -- skrypt
	CGI do zarz�dzania baz� pyta� FAQ. THE FREEZE SCRIPT -- Freeze
	umo�liwia "wyeksportowanie" skrypt�w w Pythonie na maszyny na
	kt�rych nie jest on zainstalowany.  programs to people who don't
	have Python.

	IDLE -- a Tkinter-based IDE for Python
	modulator -- generuje kod w C do pisania nowych modu��w dla Pythona.
	Pynche -- The PYthonically Natural Color and Hue Editor
	Webchecker -- Prosty program przeszukij�cy drzewo WWW w poszukiwaniu
		      na przyk�ad nie istniej�cych link�w.
	world -- wy�wietla nazwy pa�stw i odpowiadaj�ce im domeny w DNS

%description -l pl demos
Ten pakiet zawiera przyk�adowe programy i narz�dzia znajduj�ce si� w 
�r�d�owej dystrybucji Pythona.

Dema obrazuj� prawie wszystkie cechy Pythona i zastosowania w kt�rych mo�e
on by� u�yty.

Zawatre w pakiecie narz�dzia to:

	audiopy - program do sterowania urz�dzeniem dzwi�kowym w Solarisie.
	BGEN -- Automatyczny generator modu��w rozszerzaj�cych.
	FAQ Wizard -- skrypt CGI do zarz�czania baz� pyta� (FAQ).
	THE FREEZE SCRIPT -- Freeze make it possible to ship arbitrary Python
			 programs to people who don't have Python.
	IDLE -- napisane z Tkinter �rodowisko programistyczne (IDE) do Pythona
	modulator -- a generator of boilerplate code for modules to be written in C.
	Pynche -- The PYthonically Natural Color and Hue Editor
	Webchecker -- This is a simple web tree checker, useful to find bad links in
								a web tree.
	world -- Print mappings between country names and DNS country codes

%package gdbm
Summary:	Python interface to the GDBM library
Summary(pl):	Interfejs do biblioteki GDBM dla Pythona
Group:		Development/Languages/Python
Group(pl):	Programowanie/J�zyki/Python
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
Interfejs do biblioteki (n)curses. curses do biblioteka uno�liwiaj�ce tworzenie
okienkowego interfejsu u�ytkownika na terminalu tekstowym.

%package zlib
Summary:	Python interface to the zlib library
Summary(pl):	Interfejs do biblioteki zlib  dla Pythona
Group:		Development/Languages/Python
Group(pl):	Programowanie/J�zyki/Python
Icon:		linux-python-zlib-icon.gif
Requires:	%{name} =%{version}

%description zlib
An interface to the zlib library. zlib offers the gzip algorithms for
applications programmers.

%description -l pl zlib
Interfejs do biblioteki zlib dla Pythona. Zlib udost�pnia algorytmy
kompresji u�ywane przez gzip'a.

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
* Sun Jun  6 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5.2-1]
- based on RH spec,
- spec rewrited by PLD team,
- pl translation by Wojtek �lusarczyk <wojtek@shadow.eu.org>.
