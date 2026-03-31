import "./App.css";

function App() {

  return (
    <>
      <section id="center">
        <h1>
          Loco Data Miner
        </h1>

        {/* Upload Area */}
        <div className="upload-box">
          <div className="upload-label">
            Upload Here
          </div>
          <input type="file" />
        </div>
      </section>
    </>
  );
}

export default App;
