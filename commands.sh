# Create PostgreSQL database in Docker container
docker run --name db_scrapad -p 5432:5432 -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=db_scrapad -d postgres

# Create Postgre GUI with pgAdmin
docker pull dpage/pgadmin4:latest
docker run --name pgadmin4 -p 5051:80 -e "PGADMIN_DEFAULT_EMAIL=inaki.garcianoya@gmail.com" -e "PGADMIN_DEFAULT_PASSWORD=password" -d dpage/pgadmin4

# Alembic commands
alembic revision -m "init"
alembic upgrade head

# Activate environment 
source .venv/Scripts/activate

# Graphql queries
mutation { 
  createAd(name: "33333444", amount: 111, price: 122222){
  	  uuid
      name
      price
      amount
      material
  }
}

query {
  getAd(id: "2390a967-4aa4-4c74-ab14-005ee609d546") {
    ad {
      uuid
      name
      price
      amount
      material
    }
    errors
  }
}

query {
  getDetail(id: "f0d0-47e9-899f-2aefa5c6fcff") {
    ad {
      uuid
      name
      price
      amount
      material
    }
    relatedads {
      uuid
      name
      price
      amount
      material
    }
    errors
  }
}

query {
  getPage(term: "Alumnio con zinc en lingotes", perPage: 2, nPage:1) {
    page {
      ads {
        uuid
        material
      }
      total
      current
      nextPage
    }
    errors
  }
}

# Add users to the database (SQL)
INSERT INTO ads(uuid,"name",amount,price,material) VALUES ('25393260-f0d0-47e9-899f-2aefa5c6fcff','Vendo cobre',12,180,'cobre');
INSERT INTO ads(uuid,"name",amount,price,material) VALUES ('b434b963-ad9f-47db-b22e-e8d5c04d4e70','Lingotes de cobre',10,1500,'cobre');
INSERT INTO ads(uuid,"name",amount,price,material) VALUES ('b434b963-ad9f-47db-b22e-e8d5c04d4e70','Lingotes de cobre',10,1500,'lingotes');
INSERT INTO ads(uuid,"name",amount,price,material) VALUES ('d4534c4a-048d-47b2-b8d1-df61c2c46093','Alumnio con zinc en lingotes',5,2800,'lingotes');
INSERT INTO ads(uuid,"name",amount,price,material) VALUES ('d4534c4a-048d-47b2-b8d1-df61c2c46093','Alumnio con zinc en lingotes',5,2800,'aluminio');
INSERT INTO ads(uuid,"name",amount,price,material) VALUES ('d4534c4a-048d-47b2-b8d1-df61c2c46093','Alumnio con zinc en lingotes',5,2800,'zinc');
INSERT INTO ads(uuid,"name",amount,price,material) VALUES ('99f4e074-577f-45d4-af9d-936d229cc459','Lingotón de bronce',8,4500,'bronce');
INSERT INTO ads(uuid,"name",amount,price,material) VALUES ('99f4e074-577f-45d4-af9d-936d229cc459','Lingotón de bronce',8,4500,'lingoton');
INSERT INTO ads(uuid,"name",amount,price,material) VALUES ('223c983b-f32d-4b06-b17d-16061dead330','Briquetas de cobre',50,4700,'briquetas');
INSERT INTO ads(uuid,"name",amount,price,material) VALUES ('223c983b-f32d-4b06-b17d-16061dead330','Briquetas de cobre',50,4700,'cobre');
INSERT INTO ads(uuid,"name",amount,price,material) VALUES ('1a0912bc-3e9d-4550-8460-3d4811a3c8b0','Briquetas de aluminio',0,7800,'briquetas');
INSERT INTO ads(uuid,"name",amount,price,material) VALUES ('1a0912bc-3e9d-4550-8460-3d4811a3c8b0','Briquetas de aluminio',0,7800,'aluminio');
INSERT INTO ads(uuid,"name",amount,price,material) VALUES ('8e742af4-9fb2-4d1a-9174-2b260b9c71b0','Botellas de plástico',15,500,'plastico');
INSERT INTO ads(uuid,"name",amount,price,material) VALUES ('520c61fb-854e-4a7f-aacf-3d5c8cb4dbc1','Lingotes',10,5470,'aluminio');
INSERT INTO ads(uuid,"name",amount,price,material) VALUES ('520c61fb-854e-4a7f-aacf-3d5c8cb4dbc1','Lingotes',10,5470,'lingotes');
INSERT INTO ads(uuid,"name",amount,price,material) VALUES ('2390a967-4aa4-4c74-ab14-005ee609d546','Mallas de plastico',4,800,'plastico');
INSERT INTO ads(uuid,"name",amount,price,material) VALUES ('2390a967-4aa4-4c74-ab14-005ee609d546','Mallas de plastico',4,800,'otros');
