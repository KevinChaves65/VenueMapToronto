from __future__ import annotations
from typing import Dict, Literal
from datetime import datetime, timezone
from pydantic import BaseModel, Field, HttpUrl, constr, field_validator, model_validator, NonNegativeFloat

EventStatus = Literal["onsale", "offsale", "cancelled", "postponed", "unknown"]
TitleStr = constr(min_length=1, max_length=200)
ShortStr = constr(min_length=1, max_length=120)

class TimeStamped(BaseModel):
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    @model_validator(mode="after")
    def _ensure_tz(self):
        for k in ("created_at", "updated_at"):
            dt = getattr(self, k)
            if dt.tzinfo is None:
                setattr(self, k, dt.replace(tzinfo=timezone.utc))
        return self

class SourceRefs(BaseModel):
    ids: Dict[str, str] = Field(default_factory=dict)

class GeoPoint(BaseModel):
    longitude: float
    latitude: float
    @field_validator("longitude")
    @classmethod
    def _lon(cls, v: float) -> float:
        if not -180 <= v <= 180: raise ValueError("longitude must be between -180 and 180")
        return v
    @field_validator("latitude")
    @classmethod
    def _lat(cls, v: float) -> float:
        if not -90 <= v <= 90: raise ValueError("latitude must be between -90 and 90")
        return v
    def as_geojson(self): return {"type":"Point","coordinates":[self.longitude, self.latitude]}

class Price(BaseModel):
    min: NonNegativeFloat = 0
    max: NonNegativeFloat = 0
    currency: ShortStr = "CAD"
    @model_validator(mode="after")
    def _bounds(self):
        if self.max < self.min:
            raise ValueError("price.max must be >= price.min")
        return self
