class Cuboid:
    def __init__(self, state: bool, x0: int, x1: int, y0: int, y1: int, z0: int, z1: int):
        self.on_off = state
        self.x_from = x0
        self.x_to = x1
        self.y_from = y0
        self.y_to = y1
        self.z_from = z0
        self.z_to = z1

    def copy(self):
        return Cuboid(self.on_off, self.x_from, self.x_to, self.y_from, self.y_to, self.z_from, self.z_to)

    def trim(self, trimmer):
        return self if trimmer is None \
            else Cuboid(self.on_off,
                        max(self.x_from, trimmer.x_from),
                        min(self.x_to, trimmer.x_to),
                        max(self.y_from, trimmer.y_from),
                        min(self.y_to, trimmer.y_to),
                        max(self.z_from, trimmer.z_from),
                        min(self.z_to, trimmer.z_to)) \
            if not self.disjoint(trimmer) \
            else None

    def rotated_cw(self):
        return Cuboid(self.on_off, self.y_from, self.y_to, self.z_from, self.z_to, self.x_from, self.x_to)

    def rotated_ccw(self):
        return Cuboid(self.on_off, self.z_from, self.z_to, self.x_from, self.x_to, self.y_from, self.y_to)

    def volume(self):
        return (self.x_to - self.x_from + 1) * (self.y_to - self.y_from + 1) * (self.z_to - self.z_from + 1)

    def covers(self, other):
        """@self fully covers @other"""
        return _cover_1d(self.x_from, self.x_to, other.x_from, other.x_to) \
            and _cover_1d(self.y_from, self.y_to, other.y_from, other.y_to) \
            and _cover_1d(self.z_from, self.z_to, other.z_from, other.z_to)

    def disjoint(self, other):
        """
        Check if @self and @other are disjoint
        :param other: another cuboid
        :return: whether @self is disjoint from @other
        """
        return _disjoint_1d(self.x_from, self.x_to, other.x_from, other.x_to) \
            or _disjoint_1d(self.y_from, self.y_to, other.y_from, other.y_to) \
            or _disjoint_1d(self.z_from, self.z_to, other.z_from, other.z_to)

    def _split_x(self, other):
        """
        Cut @other to up to 3 cuboids, each one has its x axes either fully inside
        @self x axes or fully outside.
        """
        if self.disjoint(other):
            return [other]
        result = []
        if other.x_from < self.x_from:
            c = other.copy()
            c.x_to = self.x_from - 1
            result.append(c)
        if other.x_to > self.x_to:
            c = other.copy()
            c.x_from = self.x_to + 1
            result.append(c)
        c = other.copy()
        c.x_from = max(self.x_from, other.x_from)
        c.x_to = min(self.x_to, other.x_to)
        result.append(c)
        return [r for r in result if not self.covers(r)]

    def dismantle(self, other):
        """
        Returns a list of cuboids disjoint from @self which union
        is the part of @other not covered by @self.
        """
        if self.covers(other):
            return []
        elif self.disjoint(other):
            return [other]
        cuboids_x = self._split_x(other)
        cuboids_y = []
        for cx in cuboids_x:
            cuboids_y += [cy.rotated_cw() for cy in self.rotated_ccw()._split_x(cx.rotated_ccw())]
        cuboids_z = []
        for cy in cuboids_y:
            cuboids_z += [cz.rotated_ccw() for cz in self.rotated_cw()._split_x(cy.rotated_cw())]
        return cuboids_z

    def __str__(self):
        return "{{{} : {}..{}, {}..{}, {}..{}}}".format(
            "on" if self.on_off else "off",
            self.x_from, self.x_to, self.y_from, self.y_to, self.z_from, self.z_to)


def _disjoint_1d(c1_from, c1_to, c2_from, c2_to):
    return c2_from > c1_to or c2_to < c1_from


def _cover_1d(c1_from, c1_to, c2_from, c2_to):
    return c1_from <= c2_from and c2_to <= c1_to
