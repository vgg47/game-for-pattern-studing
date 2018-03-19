#pragma once
 
#include <memory>
#include "Gondor_pers.h"
#include "Izengard_pers.h"


class Factory_pers {
public:
	Factory_pers();
	virtual std::unique_ptr<Unit> create_unit();
};

class Archer_factory : public Factory_pers {
	Archer_factory();

	std::shared_ptr<Unit> Create_unit() override;
};

class Knight_factory : public Factory_pers {
	Knight_factory();

	std::shared_ptr<Unit> Create_unit() override;
};

class Guardian_citadeles_factory : public Factory_pers {
	Guardian_citadeles_factory();

	std::shared_ptr<Unit> Create_unit() override;
};

class Pathfinder_factory : public Factory_pers {
	Pathfinder_factory();

	std::shared_ptr<Unit> Create_unit() override;
};

class Siege_gun_factory : public Factory_pers {
	Siege_gun_factory();

	std::shared_ptr<Unit> Create_unit() override;
};

class Orc_worker_factory : public Factory_pers {
	Orc_worker_factory();

	std::shared_ptr<Unit> Create_unit() override;
};

class Uruk_hai_factory : public Factory_pers {
	Uruk_hai_factory();

	std::shared_ptr<Unit> Create_unit() override;
};

class Uruk_shooter_factory : public Factory_pers {
	Uruk_shooter_factory();

	std::shared_ptr<Unit> Create_unit() override;
};

class Shaman_factory : public Factory_pers {
	Shaman_factory();

	std::shared_ptr<Unit> Create_unit() override;
};

class Horseman_factory : public Factory_pers {
	Horseman_factory();

	std::shared_ptr<Unit> Create_unit() override;
}

class Ram_factory : public Factory_pers {
	Ram_factory();

	std::shared_ptr<Unit> Create_unit() override;
}