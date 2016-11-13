table "dataset_params" do
	column "id", :key, :as => :integer
	column "date", :date
	column "name", :string
	column "mean", :string
	column "median", :string
	column "rms", :string
	column "min", :string
	column "max", :string
	column "telescope", :string
end

table "datasets" do
	column "id", :key, :as => :integer
	column "date", :date
	column "rawdata", :text
end

