.DEFAULT_GOAL := repodata

pcb:
#	-rpmbuild -bs SPECS/pcb-4.0.0-?.spec --clean
#	-rpmbuild -bs SPECS/pcb-4.0.1-?.spec --clean
#	-rpmbuild -bs SPECS/pcb-4.0.2-?.spec --clean
#	-rpmbuild -bs SPECS/pcb-4.1.0-?.spec --clean
#	-rpmbuild -bs SPECS/pcb-4.1.1-?.spec --clean
#	-rpmbuild -bs SPECS/pcb-4.1.2-?.spec --clean
#	-rpmbuild -bs SPECS/pcb-4.1.3-?.spec --clean
#	-rpmbuild -bs SPECS/pcb-4.2.0-?.spec --clean
	-rpmbuild -bs SPECS/pcb-4.2.1-?.spec --clean

#	-rpmbuild -bb SPECS/pcb-4.0.0-?.spec --clean
#	-rpmbuild -bb SPECS/pcb-4.0.1-?.spec --clean
#	-rpmbuild -bb SPECS/pcb-4.0.2-?.spec --clean
#	-rpmbuild -bb SPECS/pcb-4.1.0-?.spec --clean
#	-rpmbuild -bb SPECS/pcb-4.1.1-?.spec --clean
#	-rpmbuild -bb SPECS/pcb-4.1.2-?.spec --clean
#	-rpmbuild -bb SPECS/pcb-4.1.3-?.spec --clean
#	-rpmbuild -bb SPECS/pcb-4.2.0-?.spec --clean
	-rpmbuild -bb SPECS/pcb-4.2.1-?.spec --clean

pcb-dox:
#	-rpmbuild -bb SPECS/pcb-dox-4.0.0-?.spec --clean
#	-rpmbuild -bb SPECS/pcb-dox-4.0.1-?.spec --clean
#	-rpmbuild -bb SPECS/pcb-dox-4.0.2-?.spec --clean
#	-rpmbuild -bb SPECS/pcb-dox-4.1.0-?.spec --clean
#	-rpmbuild -bb SPECS/pcb-dox-4.1.1-?.spec --clean
#	-rpmbuild -bb SPECS/pcb-dox-4.1.2-?.spec --clean
#	-rpmbuild -bb SPECS/pcb-dox-4.1.3-?.spec --clean
#	-rpmbuild -bb SPECS/pcb-dox-4.2.0-?.spec --clean
	-rpmbuild -bb SPECS/pcb-dox-4.2.1-?.spec --clean

check:
	-rpmlint -v RPMS > logs/RPMS.log
	-rpmlint -v SPECS > logs/SPECS.log
	-rpmlint -v SRPMS > logs/SRPMS.log

repodata:
	-createrepo --update --database .

