#
# Conditional build:
%bcond_without	tkinter			# disables tkinter module building
%bcond_without	tests			# disables Python testing
%bcond_with	verbose_tests		# runs tests in verbose mode
#
# tests which will not work on 64-bit platforms
%define		no64bit_tests	test_audioop test_rgbimg test_imageop
# tests which may fail because of builder environment limitations (no /proc or /dev/pts)
%define		nobuilder_tests test_resource test_openpty test_socket test_nis test_posix test_locale test_pty
# tests which fail because of some unknown/unresolved reason (this list should be empty)
%define		broken_tests test_anydbm test_bsddb test_re test_shelve test_whichdb test_zipimport test_distutils
# test_distutils fails for unknown reason:
# AssertionError: '/tmp/tmpaomC0l/installation/share/python' != '/tmp/tmpaomC0l/installation/lib/python'

%define py_ver		2.4
%define py_prefix	%{_prefix}
%define py_libdir	%{py_prefix}/%{_lib}/python%{py_ver}
%define py_incdir	%{_includedir}/python%{py_ver}
%define py_sitedir	%{py_libdir}/site-packages
%define py_dyndir	%{py_libdir}/lib-dynload

Summary:	Very high level scripting language with X interface
Summary(es):	Lenguaje script de alto nivel con interfaz X
Summary(fr):	Langage de script de tr�s haut niveau avec interface X
Summary(pl):	Python - j�zyk obiektowy wysokiego poziomu
Summary(pt_BR):	Linguagem de programa��o interpretada de alto n�vel
Summary(ru):	���� ���������������� ����� �������� ������ � X-�����������
Summary(tr):	X aray�zl�, y�ksek d�zeyli, kabuk yorumlay�c� dili
Summary(uk):	���� ������������� ���� �������� Ҧ��� � X-�����������
Name:		python
Version:	%{py_ver}
Release:	4
Epoch:		1
License:	PSF
Group:		Applications
Source0:	http://www.python.org/ftp/python/%{version}/Python-%{version}.tar.bz2
# Source0-md5:	44c2226eff0f3fc1f2fedaa1ce596533
Source1:	http://www.python.org/ftp/python/doc/%{version}/html-%{version}.tar.bz2
# Source1-md5:	10cca09fcdf1b5ad269bc9edb652d76f
Patch0:		%{name}-readline.patch
Patch1:		%{name}-%{name}path.patch
Patch2:		%{name}-default_encoding.patch
Patch3:		%{name}-no_ndbm.patch
Patch4:		%{name}-ac_fixes.patch
Patch5:		%{name}-noarch_to_datadir.patch
Patch6:		%{name}-lib64.patch
Patch7:		%{name}-doc_path.patch
URL:		http://www.python.org/
BuildRequires:	autoconf
BuildRequires:	bzip2-devel
BuildRequires:	db-devel >= 4
BuildRequires:	expat-devel >= 1:1.95.7
BuildRequires:	gdbm-devel >= 1.8.3
BuildRequires:	gmp-devel >= 4.0
BuildRequires:	ncurses-ext-devel >= 5.2
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	readline-devel >= 4.2
%{?with_tkinter:BuildRequires:	tix-devel >= 1:8.1.4-4}
%{?with_tkinter:BuildRequires:	tk-devel >= 8.4.3}
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	python-xml
Obsoletes:	python-intl
Obsoletes:	python-curses
Obsoletes:	python-gdbm
Obsoletes:	python-zlib
Obsoletes:	python2
Obsoletes:	python2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{with verbose_tests}
%define test_flags -v -l -x 
%else
%define test_flags -l -x 
%endif

%ifarch alpha amd64 ia64 ppc64 sparc64 ppc64
%define test_list %{nobuilder_tests} %{broken_tests} %{no64bit_tests}
%else
%define test_list %{nobuilder_tests} %{broken_tests}
%endif

%description
Python is an interpreted, interactive, object-oriented programming
language. It incorporates modules, exceptions, dynamic typing, very
high level dynamic data types, and classes. Python combines remarkable
power with very clear syntax. It has interfaces to many system calls
and libraries, as well as to various window systems, and is extensible
in C or C++. It is also usable as an extension language for
applications that need a programmable interface. Finally, Python is
portable: it runs on many brands of UNIX, on the Mac, and on PCs under
MS-DOS, Windows, Windows NT, and OS/2.

%description -l de
Python ist eine interpretierte, interaktive, objektorientierte
Programmiersprache, vergleichbar zu Tcl, Perl, Scheme oder Java.
Python enth�lt Module, Klassen, Exceptions, High-Level dynamische
Datentypen und dynamisches Typisieren. Python unterst�tzt Interfaces
zu vielen Systemaufrufen und Libraries, sowie verschiedene
Fenstersysteme (X11, Motif, Tk, Mac und MFC)

Programmierer k�nnen neue built-in-Module f�r Python in C oder C++
schreiben. Python kann auch als Erweiterungssprache f�r Applikationen
benutzt werden, die ein programmierbares Interface brauchen. Dieses
Paket enth�lt die meisten Standard-Python-Module, und Module zum
Ansprechen von Tix (Tk-widget set) und RPM.

%description -l es
Python es un lenguaje de scripts interpretado orientado a objetos.
Contiene soporte para carga din�mica de objetos, clases, m�dulos y
excepciones.

Es sencillo adicionar interfaces para nuevos sistemas de biblioteca a
trav�s de c�digo C, tornando Python f�cil de usar en ambientes
particulares/personalizados. Este paquete Python incluye la mayor�a de
los m�dulos padr�n Python, junto con m�dulos para crear interfaces
para el conjunto de componentes Tix para Tk y RPM.

%description -l fr
Python est un langage de script interpr�t� et orient� objet. Il g�re
le chargement dynamique des objets, les classes, les modules et les
exceptions. L'ajout d'interfaces aux nouvelles biblioth�ques syst�mes
avec du code C est simple, ce qui rend Python facile � utiliser dans
des configs personnalis�es.

Ce paquetage Python contient la plupart des modules Python standards,
ainsi que ceux permettant l'interfa�age avec les widgets Tix pour Tk
et RPM.

%description -l pl
Python jest interpretowanym, interaktywnym i zorientowanym obiektowo
j�zykiem programowania. Jest modularny, obs�uguje wyj�tki, dynamiczne
typy, zaawansowane dynamiczne struktury danych i klasy. Python ��czy w
sobie du�e mo�liwo�ci i przejrzyst� sk�adni�. Posiada interfejsy do
wielu wywo�a� systemowych i bibliotek, w tym r�wnie� do r�nych
bibliotek okienkowych. Mo�liwo�ci jego mo�na jeszcze rozszerza�
poprzez odpowiednie modu�y pisane w C lub C++. Python mo�e by� r�wnie�
u�yty jako element aplikacji, kt�rym potrzebny jest interpreter do
skrypt�w. I wreszcie, Python jest wieloplatformowy, dzia�a na wielu
odmianach UNIX-a, Macu oraz PC pod DOS-em, Windows, WindowsNT oraz
OS/2.

%description -l pt_BR
Python � uma linguagem de scripts interpretada orientada a objetos.
Cont�m suporte para carga din�mica de objetos, classes, m�dulos e
exce��es. Adicionar interfaces para novos sistemas de biblioteca
atrav�s de c�digo C � simples, tornando Python f�cil de usar em
ambientes particulares/personalizados.

Este pacote Python inclui a maioria do m�dulos padr�o Python, junto
com m�dulos para interfaceamento para o conjunto de componentes Tix
para Tk e RPM.

%description -l ru
Python - ��� ����������������, ��������-��������������� ����
����������������. �� ������������ ������������ �������� ��������,
������, ������ � ��������� �������������� �������� (exceptions).
�������� ���������� ����������� � ����� ��������� ����������� �����
��� �� ����� C ������ Python ������� ������� ��� ������������� �
����������� �������������.

%description -l tr
Python, nesneye y�nelik bir kabuk yorumlay�c�d�r. Nesnelerin,
s�n�flar�n, mod�llerin ve ayk�r� durumlar�n dinamik y�klenmelerine
destek verir. C koduyla birlikte kullan�m� son derece kolayd�r. Bu
paket, standart Python birimlerinin �o�unun yan�s�ra Tk ve RPM i�in
aray�z birimlerini de i�erir.

%description -l uk
Python - �� ��������������, ��'�����-�Ҧ�������� ���� �������������.
��� Ц�����դ ����ͦ��� �������� ��'��Ԧ�, �����, ����̦ �� �������
��������� �����æ� (exceptions). �������� ��������� ��������Ӧ� ���
����� ��������� ¦�̦���� ����� ��� �� ��צ C ������ Python ������
������� ��� ������������ � ���æ������ ���Ʀ����æ��.

%package libs
Summary:	Python library
Summary(pl):	Biblioteka j�zyka Python
Group:		Libraries/Python
Provides:	python(bytecode) = %{py_ver}

%description libs
Python library.

%description libs -l pl
Biblioteka j�zyka Python.

%package modules
Summary:	Python modules
Summary(pl):	Modu�y j�zyka Python
Group:		Libraries/Python
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	python-logging
Obsoletes:	python-optik
Obsoletes:	python-xmlrpc <= 1.0.1

%description modules
Python modules.

%description modules -l pl
Modu�y j�zyka Python.

%package -n pydoc
Summary:	Python interactive module documentation access support
Summary(pl):	Interaktywne korzystanie z dokumentacji modu��w j�zyka Python
Group:		Applications
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	python-pydoc

%description -n pydoc
Python interactive module documentation access support.

%description -n pydoc -l pl
Interaktywne korzystanie z dokumentacji modu��w j�zyka Python.

%package -n idle
Summary:	IDE for Python language
Summary(pl):	IDE dla j�zyka Python
Group:		Applications
Requires:	%{name}-tkinter = %{epoch}:%{version}-%{release}
Obsoletes:	python-idle

%description -n idle
IDE for Python language.

%description -n idle -l pl
IDE dla j�zyka Python.

%package devel
Summary:	Libraries and header files for building python code
Summary(de):	Libraries und Header-Dateien zum Erstellen von Python-Code
Summary(es):	Bibliotecas y archivos de inclusi�n para construir programas en python
Summary(fr):	Biblioth�ques et en-t�tes pour construire du code python
Summary(pl):	Pliki nag��wkowe i biblioteki Pythona
Summary(pt_BR):	Bibliotecas e arquivos de inclus�o para o Python
Summary(ru):	���������� � ������ ��� ���������� ���� �� ����� Python
Summary(tr):	Python ile geli�tirme yapmak i�in gerekli dosyalar
Summary(uk):	��̦����� �� ������ ��� ������������� �� ��צ Python
Group:		Development/Languages/Python
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
The Python interpreter is relatively easy to extend with dynamically
loaded extensions and to embed in other programs. This package
contains the header files and libraries which are needed to do both of
these tasks.

%description devel -l de
Der Python-Interpretierer ist relativ einfach anhand von dynamisch
ladbaren Erweiterungen auszubauen und l��t sich in andere Programme
integrieren. Dieses Paket enth�lt die Header-Dateien und Libraries,
die f�r beide Aufgaben erforderlich sind.

%description devel -l es
El interpretador Python permite incluir con facilidad extensiones
cargadas din�micamente. Python es tambi�n f�cil de ser empotrado en
otros programas. Este paquete contiene los archivos de inclusi�n y
bibliotecas necesarios para estas dos tareas.

%description devel -l fr
L'interpr�teur Python est relativement facile � �tendre avec des
extensions charg�es dynamiquement et � ins�rer dans d'autres
programmes. Ce paquetage contient les en-t�tes et les biblioth�ques
n�cessaires � ces deux t�ches.

%description devel -l pl
Interpreter Pythona jest w miar� �atwy do rozszerzania przy pomocy
dynamicznie �adowanych rozszerze� napisanych w C lub C++ oraz
osadzania w innych programach. Ten pakiet zawiera pliki nag��wkowe i
wszystko inne co potrzebne do tych cel�w.

%description devel -l pt_BR
O interpretador Python permite incluir com facilidade extens�es
carregadas dinamicamente. Python � tamb�m f�cil de ser embutido em
outros programas. Este pacote cont�m os arquivos de inclus�o e
bibliotecas necess�rios para estas duas tarefas.

%description devel -l ru
������������� Python ������������ ����� ����������� ��� ������
����������� ����������� ���������� � ������������ � ������ ���������.
���� ����� �������� ������ � ����������, ����������� ��� ����� ����
�����.

%description devel -l tr
Bu paket, Python ile geli�tirme yap�labilmesi i�in gerekli ba�l�k
dosyalar�n� ve kitapl�klar� i�erir.

%description devel -l uk
������������� Python צ������ ����� ������������ �� ���������
��������� � ����ͦ���� ��������� �� ������դ���� � ��ۦ ��������. ���
����� ͦ����� ������ �� ¦�̦�����, ����Ȧ�Φ ��� ���� ��� �����.

%package devel-src
Summary:	Python module sources
Summary(pl):	Pliki �r�d�owe modu��w Pythona
Group:		Development/Languages/Python
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description devel-src
Python module sources.

%description devel-src -l pl
Pliki �r�d�owe modu��w Pythona.

%package devel-tools
Summary:	Python development tools
Summary(pl):	Narz�dzia programistyczne j�zyka Python
Group:		Development/Languages/Python
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description devel-tools
Python development tools such as profilers and debugger.

%description devel-tools -l pl
Narz�dzia programistyczne j�zyka Python takie jak profiler oraz debugger.

%package static
Summary:	Static python library
Summary(pl):	Statyczna biblioteka Pythona
Group:		Development/Languages/Python
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static python library.

%description static -l pl
Statyczna biblioteka Pythona.

%package doc
Summary:	Documentation on Python
Summary(de):	Dokumentation zu Python
Summary(es):	Documentaci�n para Python
Summary(fr):	Documentation sur Python
Summary(pl):	Dokumentacja do Pythona
Summary(pt_BR):	Documenta��o para a linguagem de programa��o Python
Summary(ru):	������������ �� ����� Python
Summary(tr):	Python belgeleri
Summary(uk):	���������æ� �� ��צ Python
Group:		Documentation
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	python-docs

%description doc
This package contains documentation on the Python language and
interpretor as a mix of plain ASCII files and LaTeX sources.

%description doc -l de
Dieses Paket enth�lt Dokumentationen zu Python (Sprache und
Interpreter) in Form von einfachen ASCII-Dateien und LaTeX-Quellen.

%description doc -l es
Documentaci�n para Python. Contiene archivos en texto y PostScript.

%description doc -l fr
Ce paquetage contient la documentation sur le langage python et sur
son interpr�teur sous forme de fichiers ASCII et LaTeX.

%description doc -l pl
Oficjalna dokumentacja do Pythona. Zawiera przyk�adowe programy,
narz�dzia i dokumentacj�. Strony podr�cznika man znajduj� si� w
g��wnym pakiecie. Ten pakiet nie zawiera �r�de� dokumentacji
napisanych w LaTeXu, tylko gotowe do wykorzystania pliki
postscriptowe i HTML.

%description doc -l pt_BR
O pacote python-doc cont�m documenta��o para a linguagem de
programa��o e para o interpretador Python. Fornecida em arquivos texto
e Postcript.

%description doc -l ru
���� ����� �������� ������������ �� ���������� ����� Python � ��
������������ ��� �������������� � ���� ������ ��������� ������ �
�������� ������� � ������� LaTeX.

%description doc -l tr
Bu paket, Python dili ile ilgili belgeleri ve d�z ASCII dosyalar� ve
LaTeX kaynaklar�n�n bir kar���m� olan yorumlay�c�y� i�erir.

%description doc -l uk
��� ����� ͦ����� ���������æ� �� ������ ��צ Python �� �� �����������
�� �������������� � �����Ħ ������ ��������� ���̦� �� ��Ȧ����
����Ԧ� � �����Ԧ LaTeX.

%package tkinter
Summary:	Standard Python interface to the Tk GUI toolkit
Summary(de):	Grafische Tk-Schnittstelle f�r Python
Summary(es):	Interfaz de GUI Tk para Python
Summary(fr):	Interface graphique Tk pour Python
Summary(pl):	Standardowy interfejs Pythona do biblioteki Tk
Summary(pt_BR):	Interface GUI Tk para Phyton
Summary(tr):	Python i�in grafik kullan�c� aray�z�
Group:		Libraries/Python
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Requires:	tcl >= 8.4.3
Requires:	tix >= 1:8.1.4-4
Requires:	tk >= 8.4.3
Obsoletes:	tkinter

%description tkinter
Standard Python interface to the Tk GUI toolkit.

%description tkinter -l de
Eine grafische Schnittstelle f�r Python, basierend auf Tcl/Tk, und von
vielen Konfigurations-Tools genutzt.

%description tkinter -l es
Una interfaz gr�fica para Python, basada en Tcl/Tk, y usada por
muchas herramientas de configuraci�n.

%description tkinter -l fr
Interface graphique pour Python, bas�e sur Tcl/Tk et utilis�e par
beaucoup des outils de configuration.

%description tkinter -l pl
Standardowy interfejs Pythona do biblioteki Tk.

%description tkinter -l pt_BR
Uma interface gr�fica para Python, baseada em Tcl/Tk, e usada por
muitas ferramentas de configura��o.

%description tkinter -l ru
����������� ��������� (GUI) ��� Python, ����������� �� Tcl/Tk.

%description tkinter -l tr
Python i�in Tcl/Tk'ye dayal� ve pek �ok ayarlama arac� taraf�ndan
kullan�lan grafik bir aray�zd�r.

%description tkinter -l uk
���Ʀ���� ��������� (GUI) ��� Python, ����������� �� Tcl/Tk.

%package old
Summary:	Deprecated Python modules
Summary(pl):	Nieaktualne modu�y j�zyka Python
Group:		Libraries/Python
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description old
Install this package when one of your program written in Python is old
as Miss Universum of 1918, who only you want to see... ooops, which
only you want to run.

%description old -l pl
Zainstaluj ten pakiet, wtedy kiedy jeden z Twoich program�w napisanych
w j�zyku Python jest tak stary jak Miss Universum z roku 1918, kt�r�
tylko ty chcesz zobaczy�... przepraszam, kt�ry tylko ty chcesz
uruchomi�.

%package examples
Summary:	Example programs in Python
Summary(pl):	Przyk�adowe programy w Pythonie
Group:		Development/Languages/Python
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes:	python-tools

%description examples
Example programs in Python.

These are for Python 2.3.4, not %{version}.

%description examples -l pl
Przyk�adowe programy w Pythonie.

Przyk�ady te s� dla Pythona 2.3.4, nie %{version}.

%prep
%setup -q -n Python-%{version}
%patch0 -p1
%patch1 -p1
# should be already fixed in the source but seems not to be:
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%if "%{_lib}" == "lib64"
%patch6 -p1
%endif
%patch7 -p1

tar -xf %{SOURCE1} --use=bzip2

%build
sed -i -e 's#-ltermcap#-ltinfo#g' configure*
%{__autoconf}
CPPFLAGS="-I%{_includedir}/ncurses"; export CPPFLAGS
%configure \
	--with-threads \
	--with-cxx=%{__cxx} \
	--enable-unicode=ucs4 \
	--enable-shared

%{__make} \
	OPT="%{rpmcflags}"

LC_ALL=C
export LC_ALL
%if %{with tests}
binlibdir=`echo build/lib.*`
%{__make} test \
	TESTOPTS="%{test_flags} %{test_list}" \
	TESTPYTHON="LD_LIBRARY_PATH=`pwd` PYTHONHOME=`pwd` PYTHONPATH=`pwd`/Lib:$binlibdir ./python -tt"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}} \
	$RPM_BUILD_ROOT{%{py_sitedir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install Makefile.pre.in $RPM_BUILD_ROOT%{py_libdir}/config

install libpython%{py_ver}.a $RPM_BUILD_ROOT%{_libdir}
ln -sf libpython%{py_ver}.a $RPM_BUILD_ROOT%{_libdir}/libpython.a
ln -sf libpython%{py_ver}.so.1.0 $RPM_BUILD_ROOT%{_libdir}/libpython.so
ln -sf libpython%{py_ver}.so.1.0 $RPM_BUILD_ROOT%{_libdir}/libpython%{py_ver}.so

rm -f $RPM_BUILD_ROOT%{_bindir}/python%{py_ver}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -ar Tools Demo $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

SCRIPT_EXT=".py"
export SCRIPT_EXT

# create several useful scripts, such as timeit.py, profile.py, pdb.py, smtpd.py
for script in timeit profile pdb pstats smtpd; do
    cat <<END > $RPM_BUILD_ROOT%{_bindir}/${script}$SCRIPT_EXT
#!/bin/sh
exec python %{py_scriptdir}/${script}.pyc "\$@"
END
done

# xgettext specific for Python code
install Tools/i18n/pygettext.py $RPM_BUILD_ROOT%{_bindir}/pygettext$SCRIPT_EXT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/python
%{_mandir}/man1/*

# readline support for python binary
%attr(755,root,root) %{py_dyndir}/readline.so

%files modules
%defattr(644,root,root,755)
%exclude %{py_scriptdir}/UserDict.py[co]
%exclude %{py_scriptdir}/codecs.py[co]
%exclude %{py_scriptdir}/copy_reg.py[co]
%exclude %{py_scriptdir}/locale.py[co]
%exclude %{py_scriptdir}/posixpath.py[co]
%exclude %{py_scriptdir}/pdb.py[co]
%exclude %{py_scriptdir}/profile.py[co]
%exclude %{py_scriptdir}/pstats.py[co]
%exclude %{py_scriptdir}/pydoc.py[co]
%exclude %{py_scriptdir}/site.py[co]
%exclude %{py_scriptdir}/stat.py[co]
%exclude %{py_scriptdir}/timeit.py[co]
%exclude %{py_scriptdir}/os.py[co]
%exclude %{py_scriptdir}/encodings/*.py[co]

%{py_scriptdir}/*.py[co]

#
# list .so modules to be sure that all of them are built
#

# three modules below does not work on 64-bit architectures
# see Python README file for explanation
%ifnarch alpha amd64 ia64 ppc64 sparc64
%attr(755,root,root) %{py_dyndir}/audioop.so
%attr(755,root,root) %{py_dyndir}/rgbimg.so
%attr(755,root,root) %{py_dyndir}/imageop.so
# sizeof(long) != sizeof(int), so dl module will not be built on 64-bit
# platforms
%attr(755,root,root) %{py_dyndir}/dl.so
%endif

%attr(755,root,root) %{py_dyndir}/_bisect.so
%attr(755,root,root) %{py_dyndir}/_bsddb.so
%attr(755,root,root) %{py_dyndir}/_codecs_cn.so
%attr(755,root,root) %{py_dyndir}/_codecs_hk.so
%attr(755,root,root) %{py_dyndir}/_codecs_iso2022.so
%attr(755,root,root) %{py_dyndir}/_codecs_jp.so
%attr(755,root,root) %{py_dyndir}/_codecs_kr.so
%attr(755,root,root) %{py_dyndir}/_codecs_tw.so
%attr(755,root,root) %{py_dyndir}/_csv.so
%attr(755,root,root) %{py_dyndir}/_curses.so
%attr(755,root,root) %{py_dyndir}/_curses_panel.so
%attr(755,root,root) %{py_dyndir}/_heapq.so
%attr(755,root,root) %{py_dyndir}/_locale.so
%attr(755,root,root) %{py_dyndir}/_multibytecodec.so
%attr(755,root,root) %{py_dyndir}/_random.so
%attr(755,root,root) %{py_dyndir}/_socket.so
%attr(755,root,root) %{py_dyndir}/_ssl.so
%attr(755,root,root) %{py_dyndir}/_testcapi.so
%attr(755,root,root) %{py_dyndir}/_weakref.so
%attr(755,root,root) %{py_dyndir}/array.so
%attr(755,root,root) %{py_dyndir}/binascii.so
%attr(755,root,root) %{py_dyndir}/bz2.so
%attr(755,root,root) %{py_dyndir}/cPickle.so
%attr(755,root,root) %{py_dyndir}/cStringIO.so
%attr(755,root,root) %{py_dyndir}/cmath.so
%attr(755,root,root) %{py_dyndir}/collections.so
%attr(755,root,root) %{py_dyndir}/crypt.so
%attr(755,root,root) %{py_dyndir}/datetime.so
%ifnarch sparc64
%attr(755,root,root) %{py_dyndir}/dbm.so
%endif
%attr(755,root,root) %{py_dyndir}/fcntl.so
%attr(755,root,root) %{py_dyndir}/gdbm.so
%attr(755,root,root) %{py_dyndir}/grp.so
%attr(755,root,root) %{py_dyndir}/itertools.so
%attr(755,root,root) %{py_dyndir}/linuxaudiodev.so
%attr(755,root,root) %{py_dyndir}/math.so
%attr(755,root,root) %{py_dyndir}/md5.so
%attr(755,root,root) %{py_dyndir}/mmap.so
%attr(755,root,root) %{py_dyndir}/nis.so
%attr(755,root,root) %{py_dyndir}/operator.so
%attr(755,root,root) %{py_dyndir}/ossaudiodev.so
%attr(755,root,root) %{py_dyndir}/parser.so
%attr(755,root,root) %{py_dyndir}/pwd.so
%attr(755,root,root) %{py_dyndir}/pyexpat.so
%attr(755,root,root) %{py_dyndir}/regex.so
%attr(755,root,root) %{py_dyndir}/resource.so
%attr(755,root,root) %{py_dyndir}/select.so
%attr(755,root,root) %{py_dyndir}/sha.so
%attr(755,root,root) %{py_dyndir}/strop.so
%attr(755,root,root) %{py_dyndir}/syslog.so
%attr(755,root,root) %{py_dyndir}/termios.so
%attr(755,root,root) %{py_dyndir}/time.so
%attr(755,root,root) %{py_dyndir}/timing.so
%attr(755,root,root) %{py_dyndir}/unicodedata.so
%attr(755,root,root) %{py_dyndir}/zlib.so

%dir %{py_scriptdir}/plat-*
%attr(755,root,root) %{py_scriptdir}/plat-*/regen
%{py_scriptdir}/plat-*/*.py[co]

%dir %{py_scriptdir}/bsddb
%{py_scriptdir}/bsddb/*.py[co]

%dir %{py_scriptdir}/compiler
%{py_scriptdir}/compiler/*.py[co]

%dir %{py_scriptdir}/curses
%{py_scriptdir}/curses/*.py[co]

%dir %{py_scriptdir}/distutils
%{py_scriptdir}/distutils/*.py[co]

%dir %{py_scriptdir}/distutils/command
%{py_scriptdir}/distutils/command/*.py[co]

%dir %{py_scriptdir}/email
%{py_scriptdir}/email/*.py[co]

%dir %{py_scriptdir}/logging
%{py_scriptdir}/logging/*.py[co]

%dir %{py_scriptdir}/xml
%{py_scriptdir}/xml/*.py[co]

%dir %{py_scriptdir}/xml/parsers
%{py_scriptdir}/xml/parsers/*.py[co]

%dir %{py_scriptdir}/xml/sax
%{py_scriptdir}/xml/sax/*.py[co]

%dir %{py_scriptdir}/xml/dom
%{py_scriptdir}/xml/dom/*.py[co]

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpython*.so.*

%dir %{py_dyndir}
%dir %{py_scriptdir}
%dir %{py_libdir}
%dir %{py_sitescriptdir}
%dir %{py_sitedir}

# shared modules required by python library
%attr(755,root,root) %{py_dyndir}/struct.so

# modules required by python library
%{py_scriptdir}/UserDict.py[co]
%{py_scriptdir}/codecs.py[co]
%{py_scriptdir}/copy_reg.py[co]
%{py_scriptdir}/locale.py[co]
%{py_scriptdir}/posixpath.py[co]
%{py_scriptdir}/site.py[co]
%{py_scriptdir}/stat.py[co]
%{py_scriptdir}/os.py[co]

# encodings required by python library
%dir %{py_scriptdir}/encodings
%{py_scriptdir}/encodings/*.py[co]

%files -n pydoc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pydoc
%{py_scriptdir}/pydoc.py[co]

%files -n idle
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/idle
%dir %{py_scriptdir}/idlelib
%dir %{py_scriptdir}/idlelib/Icons
%{py_scriptdir}/idlelib/*.py[co]
%{py_scriptdir}/idlelib/Icons/*
%{py_scriptdir}/idlelib/*.def

%files devel
%defattr(644,root,root,755)
%doc Misc/{ACKS,NEWS,README}
%attr(755,root,root) %{_libdir}/lib*.so
%dir %{py_incdir}
%{py_incdir}/*.h

%dir %{py_libdir}/config
%attr(755,root,root) %{py_libdir}/config/makesetup
%attr(755,root,root) %{py_libdir}/config/install-sh
%{py_libdir}/config/Makefile
%{py_libdir}/config/Makefile.pre.in
%{py_libdir}/config/Setup
%{py_libdir}/config/Setup.config
%{py_libdir}/config/Setup.local
%{py_libdir}/config/config.c
%{py_libdir}/config/config.c.in
%{py_libdir}/config/ccpython.o
%{py_libdir}/config/libpython2.4.a

%files devel-src
%defattr(644,root,root,755)
%attr(-,root,root) %{py_scriptdir}/*.py
%{py_scriptdir}/plat-*/*.py
%{py_scriptdir}/bsddb/*.py
%{py_scriptdir}/compiler/*.py
%{py_scriptdir}/curses/*.py
%{py_scriptdir}/distutils/*.py
%{py_scriptdir}/distutils/command/*.py
%{py_scriptdir}/email/*.py
%{py_scriptdir}/hotshot/*.py
%{py_scriptdir}/logging/*.py
%{py_scriptdir}/xml/*.py
%{py_scriptdir}/xml/parsers/*.py
%{py_scriptdir}/xml/sax/*.py
%{py_scriptdir}/xml/dom/*.py
%{py_scriptdir}/encodings/*.py
%{py_scriptdir}/idlelib/*.py

%files devel-tools
%defattr(644,root,root,755)
%doc Lib/profile.doc Lib/pdb.doc
%attr(755,root,root) %{_bindir}/timeit*
%attr(755,root,root) %{_bindir}/profile*
%attr(755,root,root) %{_bindir}/pdb*
%attr(755,root,root) %{_bindir}/pstats*
%attr(755,root,root) %{_bindir}/pygettext*
%attr(755,root,root) %{_bindir}/smtpd*

%attr(755,root,root) %{py_dyndir}/_hotshot.so
%dir %{py_scriptdir}/hotshot
%{py_scriptdir}/hotshot/*.py[co]
%{py_scriptdir}/pdb.py[co]
%{py_scriptdir}/profile.py[co]
%{py_scriptdir}/pstats.py[co]
%{py_scriptdir}/timeit.py[co]

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files doc
%defattr(644,root,root,755)
# FIXME
%doc Python-Docs-%{version}
%dir %{py_scriptdir}/test
%attr(-,root,root) %{py_scriptdir}/test/*
%attr(-,root,root) %{py_scriptdir}/email/test/*
%attr(-,root,root) %{py_scriptdir}/bsddb/test/*

%if %{with tkinter}
%files tkinter
%defattr(644,root,root,755)
%{py_scriptdir}/lib-tk
%attr(755,root,root) %{py_dyndir}/_tkinter.so
%endif

%files old
%defattr(644,root,root,755)
%dir %{py_scriptdir}/lib-old
%{py_scriptdir}/lib-old/*.py[co]
