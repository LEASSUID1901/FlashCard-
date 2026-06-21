function ProgressBar({ current, total }) {
  const percent = Math.round(((current) / total) * 100);

  return (
    <div className="progress-container">
      <div className="progress-track">
        <div className="progress-bar" style={{ width: `${percent}%` }} />
      </div>
      <div className="progress-info">
        <span>{percent}%</span>
        <span>{current} of {total}</span>
      </div>
    </div>
  );
}

export default ProgressBar;